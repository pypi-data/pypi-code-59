import click
from googletrans import LANGUAGES

from .utils.translator import (
    get_translated_text,
    get_detected_language_obj,
    create_translated_file,
    get_detected_file_language_obj,
)

from .utils.constants import (
    TRANSLATE_FROM_HELP,
    TRANSLATE_TO_HELP,
    SHOW_LANGUAGE_CODE_HELP,
    TRANSLATE_HELP,
    DETECT_HELP,
    OUTPUT_FILE_NAME_HELP,
    TRANSLATE_FILE_COMMAND_HELP,
    TRANSLATED_FILE_LANGUAGE_HELP,
    DETECT_FILE_COMMAND_HELP,
)
from .utils.googletrans_helpers import (
    print_all_language_codes,
    print_language_code,
)


@click.group()
def pytra():
    pass


@pytra.command(help=TRANSLATE_HELP)
@click.option('-f', '--translate-from', default='auto', help=TRANSLATE_FROM_HELP)
@click.option('-t', '--translate-to', default='en', help=TRANSLATE_TO_HELP)
@click.argument('origin_text')
def translate(translate_from, translate_to, origin_text):
    translated_text = get_translated_text(
        translate_from,
        translate_to,
        origin_text,
    )
    click.echo(translated_text)


@pytra.command(help=DETECT_HELP)
@click.argument('sentence')
def detect(sentence):
    detected_language_obj = get_detected_language_obj(sentence)
    if detected_language_obj:
        detected_language = detected_language_obj.lang
        detected_language_confidence = detected_language_obj.confidence
        click.echo(
            f'"{LANGUAGES[detected_language].title()}" was detected with '
            f'{detected_language_confidence} confidence'
        )


@pytra.command(help=SHOW_LANGUAGE_CODE_HELP)
@click.argument('language', required=False)
def show_language_code(language):
    if language:
        print_language_code(language)
    else:
        print_all_language_codes()


@pytra.command(help=TRANSLATE_FILE_COMMAND_HELP)
@click.option('-o', '--output', default='output.txt', help=OUTPUT_FILE_NAME_HELP)
@click.option('-t', '--translate-to', default='en', help=TRANSLATED_FILE_LANGUAGE_HELP)
@click.argument('original_file')
def translate_file(output, translate_to, original_file):
    create_translated_file(output, original_file, translate_to)


@pytra.command(help=DETECT_FILE_COMMAND_HELP)
@click.argument('file')
def detect_file(file):
    detected_language_obj = get_detected_file_language_obj(file)

    # If there was FileNotFoundError in the line before
    # then detect_language_ob is None
    if detected_language_obj:
        detected_language = LANGUAGES[detected_language_obj.lang].title()
        confidence = detected_language_obj.confidence
        click.echo(f'{detected_language} with {confidence} confidence')


if __name__ == '__main__':
    pytra()
