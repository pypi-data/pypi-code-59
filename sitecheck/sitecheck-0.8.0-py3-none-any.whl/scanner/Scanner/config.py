"""
    Geo-Instruments
    Sitecheck scanner

Loads program configuration into a config object.

Project Instance is passed to functions as required.
Configuration uses argument to load file, but if empty will prompt for a
location.

http://docs.python.org/library/configparser.html

"""
# __author__ = "Dan Edens"
# __url__= "https://github.com/DanEdens/Sitecheck_Scrapper"
# __status__  = "production"
import configparser
import os.path
import subprocess
import sys


from sitecheck.scanner.Scanner import logger, ROOT_DIR


def edit_project():
    """
    If edit flag is given, open project.ini with notepad and await file close
    Returns: wait on notepad close

    """
    if os.path.exists('bin/projects.ini'):
        pass
    else:
        generate_default()
    edit = subprocess.Popen('notepad.exe bin/projects.ini')
    return edit.wait()


def generate_default():
    """
        Than opens the generated configuration file and awaits it being closed.
            Returns (obj):
                wait object for notepad process

    """
    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['DEFAULT']['name'] = 'Test'
    config['DEFAULT']['planarray'] = '0'
    config['DEFAULT']['site'] = 'qv'
    config['DEFAULT']['skip'] = 'false'
    with open('bin/projects.ini', 'w') as configfile:
        config.write(configfile)
    edit = subprocess.Popen('notepad.exe bin/projects.ini')
    return edit.wait()


def file_dialog():
    """
        Check and use Tkinter for file dialog, or if not than generate one.
            Returns: filename
    """
    try:
        import tkinter
        from tkinter import filedialog
        options = {}
        options['defaultextension'] = '.ini'
        options['filetypes'] = [('all files', '.*'), ('Json config', '.json'), ('ini config files', '.ini')]
        options['initialdir'] = ROOT_DIR
        options['initialfile'] = 'bin/projects.ini'
        options['title'] = 'Select Project Configuration File'
        root = tkinter.Tk()
        filename = filedialog.askopenfilename(**options)
        root.destroy()
        return filename
    except ImportError:
        return generate_default()


def load_projects():
    """
    Prompts user to select projects.ini configuration\n
    [project1]\n
    skip = true\n
    group = true\n
    name = projectname1\n
    proj = null\n
    planarray = 143,124,127\n
    hassite = amp\n
    channel = test\n

    :rtype: list
    """
    # Prompt user for config file, return filename
    if os.path.isfile('bin/projects.ini'):
        config_file = 'bin/projects.ini'
    else:
        config_file = file_dialog()

    if config_file == '':
        sys.exit("Cancelled. Exiting..")
    elif not os.path.isfile(config_file):
        logger.warning("file (%s) not found. " % config_file)
        sys.exit("Exiting..")

    config = configparser.ConfigParser()
    config.read(config_file)

    return config


def check_credentials():
    """
    Query User for User and password if not preset as environmental variables.
    If User opts to save,
    Creates,runs, and deletes a bat file to setx values permanently

    Returns: env.cmd returncode

    """
    do_save = 0
    if not os.environ['SCANNER_AMPUSER']:
        logger
        os.environ['SCANNER_AMPUSER'] = input("Amp Username:")
    if not os.environ['SCANNER_AMPPASS']:
        os.environ['SCANNER_AMPPASS'] = input("Amp Password:")
        do_save = input("Save for all future runs? (y/n)")
    if do_save == 'y':
        with open('env.cmd', 'a') as file:
            file.write('setx '+os.environ['SCANNER_AMPUSER'])
            file.write('setx '+os.environ['SCANNER_AMPPASS'])
            file.write('del %0')
            file.close()
        set_env = subprocess.Popen('env.cmd')
        return set_env.wait()


class project_config():
    def __init__(self, project):
        config = configparser.ConfigParser()
        config.read('bin/projects.ini')
        self.name = config[project]['name']
        self.planarray = config[project]['planarray']
        self.site = config[project]['site']
        self.skip = config[project]['skip']
