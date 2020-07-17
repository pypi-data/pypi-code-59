import click
from googletrans import LANGCODES

from .decorators import language_name_is_correct


def print_all_language_codes():
    for (lang, code) in LANGCODES.items():
        click.echo(f'{lang} -- "{code}"')


@language_name_is_correct
def print_language_code(language):
    language = language.strip().lower()
    click.echo(f'{language.title()} -- "{LANGCODES[language]}"')
