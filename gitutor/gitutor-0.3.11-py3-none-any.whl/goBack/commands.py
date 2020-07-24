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

    full_list_of_commits = commits_full_list(repo)
    if hash:
        minihash = hash[0:7]
        selected_commit = [commit for commit in full_list_of_commits if minihash in commit]
        index_commit = [index for index in range(len(full_list_of_commits)) if minihash in full_list_of_commits[index]][0]
        if len(selected_commit) > 0:
            selected_commit = selected_commit[0]
            comment = get_comment_of_commit(selected_commit)
            index_commit += commit_before_revert(repo)
            click.echo(f'Going back to: {comment}')
            repo.git.revert([f'{minihash}..HEAD', '--no-edit'])
            full_list_of_commits = commits_full_list(repo)
            repo.git.reset(['--soft', f'HEAD~{index_commit}'])
            repo.git.commit(['-m', f'Going back to "{comment}"'])
            click.echo('Done!')

        else:
            click.echo('There is no commit with the hash provided')
    else:
        commit = prompt_for_commit_selection(full_list_of_commits, 'Select the commit you want to return')
        comment = get_comment_of_commit(commit['commit'])
        number_of_commits = full_list_of_commits.index(commit['commit'])
        if number_of_commits >= 0:
            if number_of_commits == 0:
                click.echo('Return to last commit')
            else:
                click.echo(f'Going back to "{comment}"')
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
