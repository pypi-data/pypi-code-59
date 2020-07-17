import git
import click
from PyInquirer import prompt

@click.command()
@click.pass_context
@click.option('-n', '--number', 'number' , default = 10)
def compare(ctx, number):
    '''
    Compare current status with selected commit
    '''
    #Recover repo from context
    repo = ctx.obj['REPO']

    get_options_list(repo,number)

    global question
    question = [
        {
            'type': 'list',
            'message': 'Select commit to compare',
            'name': 'commit',
            'default': 0,
            'choices': commits_to_show_plus_showmore
        }
    ]
    answer = prompt(question)
    while answer['commit'] == 'Show more commits...':
        append_more_commits(10)
        answer = prompt(question)
    answer_hash = answer['commit'][:7]
    click.echo(repo.git.diff(answer_hash))

def get_options_list(repo,number):
    global full_list_of_commits
    global commits_to_show
    global commits_to_show_plus_showmore
    full_list_of_commits = repo.git.log("--pretty=format:'%h - %s: %an, %ar'").replace("'","").splitlines()
    commits_to_show = []
    for commit in full_list_of_commits[:number]:
        commits_to_show.append(commit)

    commits_to_show_plus_showmore = commits_to_show.copy()
    commits_to_show_plus_showmore.append("Show more commits...")
    return commits_to_show_plus_showmore

def append_more_commits(number):
    for commit in full_list_of_commits[len(commits_to_show):len(commits_to_show)+number]:
        commits_to_show.append(commit)
    commits_to_show_plus_showmore = commits_to_show.copy()
    commits_to_show_plus_showmore.append("Show more commits...")
    question[0].update({'choices': commits_to_show_plus_showmore})
    question[0].update({'default': commits_to_show_plus_showmore[1]})