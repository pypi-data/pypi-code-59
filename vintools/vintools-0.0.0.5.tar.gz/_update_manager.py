def pack(package_path):
    
    """
    input  : setup_file_path : path to the setup.py file
    output : setup_file_path : path to the revised setup.py file
    
    note   : will need to update for a production-level push (i.e., 0.x.major.minor)
    """
    setup_file_path = package_path + 'setup.py'
    setup_py = open(setup_file_path, 'r')
    lines    = setup_py.readlines()
    out = open(setup_file_path, 'w')
    
    for line in lines:
        if 'version' in line:
            major, minor = line[-7:-6], line[-5:-3]
            print('Current:', line[:-2], '\n', 'Major:', major, '\n', 'Minor', minor)
            minor = str(int(minor) + 1)
            newline = line[:-7] + major + '.' + minor + line[-3:]
            update_version = '0.0.' + major + '.' + minor
            print('New:    ', newline[:-2])
            out.writelines(newline)
        else:
            out.writelines(line)
    
    print('setup.py has been updated to version:', update_version)

def git_update(package_path, commit_msg):
    
    import subprocess
    import sys
    import ipywidgets as w
    
    dist  = package_path + 'dist/*'
    setup = package_path + 'setup.py'
    
    # define args
    rm_dist    = 'rm ' + dist
    mk_wheel   = 'python3 '+ setup + ' sdist' + ' bdist_wheel'
    git_add    = 'git add *'
    git_commit = 'git commit -a -m ' + '"' + commit_msg + '"'
    git_push   = 'git push'
    
    
    # run shell processes
    subprocess.run(rm_dist,    shell = True, check = True) # done
    subprocess.run(mk_wheel,   shell = True, check = True, cwd=package_path) # done
    subprocess.run(git_add,    shell=True, check = True, cwd=package_path)
    subprocess.run(git_commit, shell=True, check = True, cwd=package_path)
    subprocess.run(git_push,   shell=True, check = True, cwd=package_path)
    
def to_pypi(package_path, pw_file, commit_msg):
    
    """
    You need a text file where 
    the first line contains only the username and the second line 
    contains only the pypi password.
    """
    pack(package_path)
    git_update(package_path, commit_msg)
    
    import subprocess
    from subprocess import PIPE
    
    username = open(pw_file, 'r').readlines()[0].strip()
    password = open(pw_file, 'r').readlines()[1].strip()
    
    twine_up = 'python3 -m twine upload -u ' + username + ' -p ' + password + ' --repository-url https://upload.pypi.org/legacy/ dist/*'

    
    twine = subprocess.run(twine_up, shell=True, cwd=package_path, stdout=PIPE)
    d = twine.stdout.decode('utf-8').split()
    for i in range(len(d)):
        if i + 1 == len(d):
            print('Upload complete. View at:',d[i])
