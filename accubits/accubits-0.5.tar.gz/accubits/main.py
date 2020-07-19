from git import Repo, RemoteProgress
import os
from shutil import rmtree
import click
from .utils import modifyProjectNamesInFiles, print_msg, show_progress

ngBoilerPlateRepo = 'git@github.com:accubits-tech/ng-boilerplate.git'



@click.group()
def cli():
    pass


@cli.command()
@click.argument('framework',  nargs=1)
@click.argument('projectname', nargs=1)
def create(framework, projectname):
    if(framework == 'ng'):
        project_path = os.getcwd() + '/' + projectname
        print_msg('Accubits CLI 1.0')
        print_msg(projectname + ' Creation Started')

        print_msg('Fetching Angular Boilerplate Repo...')
        Repo.clone_from(ngBoilerPlateRepo,project_path)
        print_msg('Completed - Boilerplate Repo Clone!')
        
        print_msg('Modify angular files to update the projectname' + projectname)
        modifyProjectNamesInFiles(project_path, projectname)
        print_msg('Modified angular files!')
        
        print_msg('Install NPM...')
        os.chdir(projectname)
        rmtree(project_path + '/.git') 
        os.system('npm i')
        print_msg('Completed - Project is Ready.')


if __name__ == "__main__":
    cli()
