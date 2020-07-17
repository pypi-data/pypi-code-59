from googletrans import Translator

from .decorators import (
    check_file_exists,
    language_code_is_correct,
    check_internet_connection,
)


translator = Translator()


@check_internet_connection
@language_code_is_correct
def get_translated_text(trans_from, trans_to, origin_text):
    translated_obj = translator.translate(
        text=origin_text,
        origin=trans_from,
        dest=trans_to,
    )
    return translated_obj.text


@check_internet_connection
def get_detected_language_obj(sentence):
    detected_language_obj = translator.detect(sentence)
    return detected_language_obj


@check_internet_connection
@language_code_is_correct
@check_file_exists
def create_translated_file(output_file_name, file_to_translate, translate_to):
    with open(output_file_name, 'w') as translated_file:
        with open(file_to_translate, 'r') as original_file:
            for line in original_file:
                translated_line = translator.translate(
                    text=line,
                    dest=translate_to,
                ).text
                translated_file.write(translated_line + '\n')


@check_internet_connection
@check_file_exists
def get_detected_file_language_obj(file):
    with open(file, 'r') as f:
        first_line = f.readline()
        return translator.detect(first_line)
