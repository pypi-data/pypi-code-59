import click

defaultBoilerPlateName = 'ng-boilerplate'


def show_progress(progress):
    with click.progressbar(progress) as i:
        for item in i:
            print(item)


def print_msg(msg, color='blue'):
    click.echo(click.style(msg, color))


def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print(
            'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def modifyProjectNamesInFiles(project_path, projectname):
    inplace_change(project_path + '/angular.json',
                   defaultBoilerPlateName, projectname)
    inplace_change(project_path + '/package.json',
                   defaultBoilerPlateName, projectname)
    inplace_change(project_path + '/e2e/src/app.e2e-spec.ts',
                   defaultBoilerPlateName, projectname)
    inplace_change(project_path + '/src/app/app.component.spec.ts',
                   defaultBoilerPlateName, projectname)
    inplace_change(project_path + '/src/app/app.component.ts',
                   defaultBoilerPlateName, projectname)
    inplace_change(project_path + '/karma.conf.js',
                   defaultBoilerPlateName, projectname)
