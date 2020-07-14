"""
Tests hang man game
"""
import pytest

from games import hangMan
from utils.file.path import find_file


def test_randomise() -> None:
    """
    tests the randomise function
    """
    file_name = 'testHangManWords.txt'
    file_path = find_file(file_name)
    if file_path is None:
        file_path = find_file(file_name, '../')

    rand_list_of_words = []
    hang_man_words = open(file_path, 'r')
    list_of_words = hang_man_words.read().split()
    for _ in list_of_words:
        rand_list_of_words.append(hangMan.randomise(file_path))
    assert rand_list_of_words != list_of_words


@pytest.mark.parametrize('word, expected',
                         [("thing", "_____"),
                          ("lol", "___"),
                          ("yellow", "______"),
                          ("discombobulate", "______________")
                          ])
def test_hiding(word: str, expected: str) -> None:
    """
    tests the hiding function
    :param word: the inputted word
    :param expected: what we expect the output to be
    """
    actual_output = hangMan.hiding(word)
    assert actual_output == expected


@pytest.mark.parametrize('guess, , expected',
                         [("a", ['_', '_', '_', '_', '_']),
                          ("i", ['_', '_', 'i', '_', '_']),
                          ("t", ['t', '_', '_', '_', '_'])
                          ])
def test_replace_space_with_guess(guess, expected) -> None:
    """
    tests the replace_space_with_guess() function
    :param guess: the user guess
    :param expected: what the function should return
    """
    list_word = ['t', 'h', 'i', 'n', 'g']
    list_hidden_word = ['_', '_', '_', '_', '_']
    actual_output = hangMan.replace_space_with_guess(guess, list_word, list_hidden_word)[0]
    assert actual_output == expected
