import git
import click
from PyInquirer import prompt
from git import GitCommandError

@click.command()
@click.pass_context
@click.option('-c', '--commit', help='Hash of commit to compare')
def compare(ctx,commit):
    '''
    Compare current status with selected commit
    '''
    #Recover repo from context
    repo = ctx.obj['REPO']

    if commit:
        try:
            click.echo(repo.git.diff(commit))
        except GitCommandError:
            click.echo('Hash not found')
        return

    full_list_of_commits = commits_full_list(repo)
    commit_page_index = 0
    choices = get_commit_page(commit_page_index, full_list_of_commits)
    question = [
        {
            'type': 'list',
            'message': 'Select commit to compare',
            'name': 'commit',
            'default': 0,
            'choices': choices
        }
    ]
    answer = prompt(question)
    while answer['commit'] == '...Show previous commits' or answer['commit'] == 'Show more commits...':
        if answer['commit'] == '...Show previous commits':
            commit_page_index-=1
            commits_to_show=get_commit_page(commit_page_index, full_list_of_commits)
        else:
            commit_page_index+=1
            commits_to_show=get_commit_page(commit_page_index, full_list_of_commits)
            click.echo(commits_to_show)
        question[0].update({'choices': commits_to_show})
        answer = prompt(question)
    answer_hash = answer['commit'][:7]
    click.echo(repo.git.diff(answer_hash))

def commits_full_list(repo):
    full_list_of_commits = repo.git.log("--pretty=format:'%h - %s: %an, %ar'").replace("'","").splitlines()
    return full_list_of_commits

def get_commit_page(page_index, full_list_of_commits):
    if page_index == 0:
        commits_to_show = full_list_of_commits[0:20]
    else:
        commits_to_show = full_list_of_commits[page_index*20:page_index*20+20]
        commits_to_show.insert(0,'...Show previous commits')
    if len(full_list_of_commits) > page_index*20+20:    
        commits_to_show.append('Show more commits...')
    return commits_to_show