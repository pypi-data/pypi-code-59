from __future__ import print_function, unicode_literals

import os
import click
from PyInquirer import prompt, print_json
from compare.commands import prompt_for_commit_selection
from compare.commands import commits_full_list
from git import GitCommandError

@click.command()
@click.pass_context
@click.option('-h', '--hash', 'hash', help="hash of the commit to go back")
def goBack(ctx, hash):
    "Returns version to a specific commit via hash, selected commit or number of commits"
    repo = ctx.obj['REPO']
    print('repo', repo)
    print('repo.index', repo.index)
    print(f"Remote from init: {repo.remote('origin').url} ")

    full_list_of_commits = commits_full_list(repo)
    print(full_list_of_commits)
    if hash:
        minihash = hash[0:7]

        selectedCommit = [commit for commit in full_list_of_commits if minihash in commit]
        if len(selectedCommit) > 0:
            selectedCommit = selectedCommit[0]
            print(selectedCommit)
            get_comment_of_commit(selectedCommit)
            commit_before_revert(repo)
            print(f'Going back to: {selectedCommit}')
            repo.git.revert([f'{minihash}..HEAD', '--no-edit'])
            print('save 1')
            full_list_of_commits = commits_full_list(repo)
            print(full_list_of_commits)
            print(minihash)
            repo.git.reset(['--soft', f'{minihash}'])
            print('save 2')
            repo.git.commit(['-m', f'Going back to: {selectedCommit}'])
            print('save 3')

        else:
            click.echo('There is no commit with the hash provided')
    else:
        commit = prompt_for_commit_selection(full_list_of_commits, 'Select the commit you want to return')
        print(commit)
        comment = get_comment_of_commit(commit['commit'])
        number_of_commits = full_list_of_commits.index(commit['commit'])
        if number_of_commits >= 0:
            if number_of_commits == 0:
                print('Return to last commit')
            else:
                print(f'Going back to "{comment}"')
            number_of_commits += commit_before_revert(repo)
            repo.git.revert([f'HEAD~{number_of_commits}..HEAD', '--no-edit'])
            repo.git.reset(['--soft', f'HEAD~{number_of_commits}'])
            repo.git.commit(['-m', f'Going back to "{comment}"'])
            click.echo('Done!')

def commit_before_revert(repo):
    click.echo('Saving changes before revert')
    repo.git.add(A=True)
    try:
        repo.git.commit("-m", 'Saving before revert')
        return 1
    except GitCommandError:
        return 0

def get_comment_of_commit(commit):
    return commit.split('- ')[1].split(':')[0]
