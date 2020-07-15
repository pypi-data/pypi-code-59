import os
import shutil
import getpass
import platform
import subprocess


class shell():
    """
        Class for standardized operating system shell commands and tools.

        Example:
        ```
        print(i6.shell.ls())
        i6.shell.cd('dir')
        print(i6.shell.pwd())
        i6.shell.mkdir('dir')
        i6.shell.touch('test.txt')
        i6.shell.rm('dir')
        print(i6.shell.cat('test.txt'))
        i6.shell.echo('test.txt', '1234', append=False)
        i6.shell.cp('src.txt', 'dst.txt')
        i6.shell.mv('src.txt', 'dst.txt')
        print(i6.shell.exists('dir'))
        print(i6.shell.which('ping'))
        print(i6.shell.user())
        print(i6.shell.uname())
        print(i6.shell.exec(['ping', '-w', '1', 'localhost']))
        i6.shell.symlink('src.txt', 'dst.txt')
        ```
    """

    def ls(path = None):
        """
            List all files in provided path, defaults to cwd.

            Example:
            ```
            print(i6.shell.ls())
            ```
        """

        return os.listdir(path)

    def cd(path = None):
        """
            Change Directory.

            Example:
            ```
            i6.shell.cd('dir')
            ```
        """

        if path is None:
            path = shell.home()

        os.chdir(path)
    
    def pwd():
        """
            Print Work Directory or cwd.

            Example:
            ```
            print(i6.shell.pwd())
            ```
        """

        return os.getcwd()
    
    def cwd():
        """
            Get Current Working Directory.

            Example:
            ```
            print(i6.shell.cwd())
            ```
        """

        return shell.pwd()

    def mkdir(path):
        """
            Create a new directory.

            Example:
            ```
            i6.shell.mkdir('dir')
            ```
        """

        os.makedirs(path)
    
    def touch(path):
        """
            Create a new file.

            Example:
            ```
            i6.shell.touch('test.txt')
            ```
        """

        if not shell.exists(path):
            with open(path, 'w'):
                pass

    def rm(path):
        """
            Remove a directory or file.

            Example:
            ```
            i6.shell.rm('dir')
            ```
        """

        if (os.path.isfile(path)) or (os.path.islink(path)):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    def cat(path, binary = False):
        """
            Read a file and return as string or bytes.

            Example:
            ```
            print(i6.shell.cat('test.txt'))
            ```
        """
        
        if binary:
            file_mode = 'rb'
            return_var = b''
        else:
            file_mode = 'r'
            return_var = ''

        if shell.exists(path):
            with open(path, file_mode) as f:
                return f.read()
        
        return return_var

    def echo(path, text, append = False):
        """
            Write to a file.

            Example:
            ```
            i6.shell.echo('test.txt', '1234', append=False)
            ```
        """
        
        file_mode = 'w'
        if append:
            file_mode = 'a'

        shell.touch(path)

        with open(path, file_mode) as f:
            f.write(text)

    def cp(src, dst):
        """
            Copy a file or folder from src to dst.

            Example:
            ```
            i6.shell.cp('src.txt', 'dst.txt')
            ```
        """

        if os.path.isfile(src):
            shutil.copy2(src, dst)
        elif os.path.isdir(src):
            shutil.copytree(src, dst)

    def mv(src, dst):
        """
            Move a file or folder from src to dst.

            Example:
            ```
            i6.shell.mv('src.txt', 'dst.txt')
            ```
        """

        shutil.move(src, dst)

    def exec(command):
        """
            Execute a command using subprocess run and return result as string.

            Example:
            ```
            print(i6.shell.exec(['ping', '-w', '1', 'localhost']))
            ```
        """

        return subprocess.run(
            command,
            stdout=subprocess.PIPE,
        ).stdout.decode().replace('\n', '')

    def exists(path):
        """
            Check if file or folder exists.

            Example:
            ```
            print(i6.shell.exists('dir'))
            ```
        """

        return (os.path.isdir(path)) or (os.path.isfile(path))

    def which(name):
        """
            Returns path to executable by the name provided.

            Example:
            ```
            print(i6.shell.which('ping'))
            ```
        """

        return shutil.which(name)
    

    def symlink(src, dst):
        """
            Create a symlink, from src to dst.

            Example:
            ```
            i6.shell.symlink('src.txt', 'dst.txt')
            ```
        """

        os.symlink(src, dst)

    def user():
        """
            Returns currently logged in user.

            Example:
            ```
            print(i6.shell.user())
            ```
        """

        return getpass.getuser()

    def home():
        """
            Returns currently logged in users home folder.

            Example:
            ```
            print(i6.shell.home())
            ```
        """

        return os.path.expanduser('~')

    def uname():
        """
            Returns current uname, platform or os.

            Example:
            ```
            print(i6.shell.uname())
            ```

            Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

            An empty string is returned if the value cannot be determined.
        """

        return platform.system()
