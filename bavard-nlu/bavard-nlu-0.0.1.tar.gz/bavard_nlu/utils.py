import collections
import json
import logging
import unicodedata
from typing import List
from google.cloud import storage
from os import getenv
import tensorflow_hub as hub
from official.nlp.bert import tokenization


def is_whitespace(char: str):
    """Checks whether `char` is a whitespace character."""
    if char == " " or char == "\t" or char == "\n" or char == "\r":
        return True
    cat = unicodedata.category(char)
    if cat == "Zs":
        return True
    return False


def get_char_to_word_map(text: str) -> List[int]:
    words = []
    char_to_word_idx = []
    prev_is_whitespace = True

    for char in text:
        if is_whitespace(char):
            prev_is_whitespace = True
            char_to_word_idx.append(len(words))

        else:
            if prev_is_whitespace:
                words.append(char)
            else:
                words[-1] += char
            prev_is_whitespace = False
            char_to_word_idx.append(len(words) - 1)
    return char_to_word_idx


def download_agent_data(bucket_name, export_file_key) -> str:
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(export_file_key)
    filename = f'/tmp/agent_data.json'
    blob.download_to_filename(filename)
    return filename


