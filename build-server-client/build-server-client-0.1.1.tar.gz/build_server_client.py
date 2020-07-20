import gzip
import os
import time
from argparse import ArgumentParser
from hashlib import md5
from itertools import cycle
from os import makedirs
from os.path import join, basename, isfile
from subprocess import check_output, call, PIPE
from tempfile import NamedTemporaryFile
from time import sleep

import humanize
import requests
from git import Repo
from requests import Response
from tqdm import tqdm


class UserError(Exception):
    def __init__(self, message, fmt='Error: {}'):
        self.fmt = fmt
        self.message = message

    def __str__(self):
        return self.fmt.format(self.message)


def guess_name(repo):
    if repo.remotes:
        url = repo.remotes[0].url
        guessed_name = url[url.rfind("/") + 1:]
        if guessed_name.endswith('.git'):
            guessed_name = guessed_name[:-len('.git')]
        return guessed_name
    return basename(repo.working_tree_dir)


def ensure_valid(server_url, project, repo):
    server_cmd = 'git config bsc.server-url "https://<some-build-server>.com"'
    project_cmd = 'git config bsc.project "{}"  # Or whatever the name is on the build server'.format(guess_name(repo))
    if not server_url and not project:
        raise UserError('Please setup your build server info with the following commands:\n\n{}\n'.format(
            '\n'.join([server_cmd, project_cmd])
        ), fmt='{}')
    if not server_url:
        raise UserError('Please setup your server url:\n\n{}\n'.format(server_cmd), fmt='{}')
    if not project:
        raise UserError('Please setup your project info:\n\n{}\n'.format(project_cmd), fmt='{}')


def ensure_success(r: Response) -> Response:
    if not r.ok:
        raise UserError('Request failed: {}'.format(r.content))
    return r


def download_visual(r, path):
    parts = []
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024
    t = tqdm(
        total=total_size, unit='iB', bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}',
        unit_scale=True, disable=total_size < 512 * 1024
    )
    for chunk in r.iter_content(block_size):
        t.update(len(chunk))
        parts.append(chunk)
    t.close()
    result = b''.join(parts)
    if total_size != 0 and len(result) != total_size:
        raise UserError('Failed to download {}!'.format(path))
    return result


def can_apply_delta():
    try:
        call(['xdelta3', '-h'], stdout=PIPE, stderr=PIPE)
        return True
    except FileNotFoundError:
        return False


def apply_delta(source_data, delta_data):
    with NamedTemporaryFile('wb') as tf1, NamedTemporaryFile('wb') as tf2, NamedTemporaryFile('rb') as tf3:
        tf1.write(source_data)
        tf2.write(delta_data)
        tf1.flush()
        tf2.flush()
        check_output(['xdelta3', '-f', '-s', tf1.name, '-d', tf2.name, tf3.name])
        data = tf3.read()
    return data


def download_artifact(request_url, output):
    params = {}
    delta_base = None
    if can_apply_delta() and isfile(output):
        with open(output, 'rb') as f:
            file_data = f.read()
        delta_base = file_data
        params['deltaBase'] = md5(file_data).hexdigest()
    r = requests.get(request_url, stream=True, params=params)
    if r.status_code == 412:
        del params['deltaBase']
        delta_base = ''
        r = requests.get(request_url, stream=True, params=params)
    ensure_success(r)
    data = download_visual(r, output)
    if delta_base:
        data = apply_delta(delta_base, data)
    with open(output, 'wb') as f:
        f.write(data)


def build_project(args):
    repo = Repo(os.getcwd(), search_parent_directories=True)
    reader = repo.config_reader()
    server_url = reader.get_value('bsc', 'server-url', default='')
    project = reader.get_value('bsc', 'project', default='')
    ensure_valid(server_url, project, repo)
    server_url = server_url.rstrip('/')
    remote_branch = repo.active_branch.tracking_branch()
    if not remote_branch:
        try:
            remote_branch = repo.remotes.origin.refs['HEAD']
        except AttributeError:
            remote_branch = next(iter(repo.remotes)).refs['HEAD']
    bases = repo.merge_base(repo.head.commit, remote_branch.commit)
    if not bases:
        raise RuntimeError('No common history between current branch and server')
    base = bases[0]
    git = repo.git
    git.commit(allow_empty=True, no_edit=True, message="Index")
    try:
        if args.untracked:
            git.add(A=True)
        raw_diff = check_output(['git', 'diff', base.hexsha, '--binary'])
    finally:
        git.reset()
        git.reset('HEAD~1', soft=True)
    diff_data = gzip.compress(raw_diff)
    print('Sending {} diff to build server...'.format(humanize.naturalsize(len(diff_data))))
    resp = ensure_success(requests.post(
        server_url + f'/{project}/build',
        files=dict(diffData=diff_data),
        params=dict(baseCommit=base.hexsha)
    )).json()
    build_id = resp['buildId']
    last_check = 0
    check_interval = 0.5
    status = {}
    for char in cycle('|/-\\'):
        print('\rCompiling... {}'.format(char), end='')
        sleep(0.1)
        if time.time() - last_check > check_interval:
            status = ensure_success(requests.get(server_url + f'/{project}/build/{build_id}')).json()
            last_check = time.time()
            if status['state'] != 'PENDING':
                break
    if status['state'] == 'FAIL':
        print('\rCompilation failed:\n{}'.format(status['error']))
    else:
        print('\rCompilation complete!')
        artifact_folder = reader.get_value('bsc', 'artifact-folder', default='build')
        makedirs(artifact_folder, exist_ok=True)
        outputs = []
        for artifact in status['artifacts']:
            output = join(artifact_folder, artifact)
            outputs.append(output)
            request_url = server_url + f'/{project}/build/{build_id}/artifacts/{artifact}'
            download_artifact(request_url, output)
        print('Artifacts:')
        for i in outputs:
            print(' - {}'.format(i))


def main():
    parser = ArgumentParser(description='Python client for a simple build server')
    sp = parser.add_subparsers(dest='action')
    sp.required = True
    p = sp.add_parser('build')
    p.add_argument('-u', '--untracked')
    args = parser.parse_args()

    handler = {
        'build': build_project
    }[args.action]
    try:
        handler(args)
    except UserError as e:
        print(str(e))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
