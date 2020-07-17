import click
from httpcore._exceptions import ConnectError


def check_file_exists(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            click.echo(f'Can\'t find specified file. Please check its name')

    return wrapper


def language_code_is_correct(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            click.echo('Language code is not correct')

    return wrapper


def language_name_is_correct(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            click.echo('Language name is not correct')

    return wrapper


def check_internet_connection(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectError:
            click.echo('Internet connection required')

    return wrapper
