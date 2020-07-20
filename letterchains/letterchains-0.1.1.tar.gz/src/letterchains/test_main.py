import pytest

from . import main


def test_subwords():
    result = set(main.subwords("ab"))
    assert result == {"a", "b"}

    result = set(main.subwords("abc"))
    assert result == {"ab", "bc", "ac"}


def test_maxes():
    assert main.maxes([1, 5, 3, 5]) == [5, 5]


def test_make_adjacency():
    result = main.make_adjacency(["a", "at", "cat", "bat", "boy", "by", "oy", "o"])
    expected = {
        "cat": {"at"},
        "bat": {"at"},
        "boy": {"by", "oy"},
        "oy": {"o"},
        "at": {"a"},
        "o": set(),
        "a": set(),
        "by": set(),
    }
    assert result == expected


@pytest.mark.parametrize(
    "input, expected", [("cat", [["cat", "at", "a"]]), ("o", [["o"]]), ("by", [["by"]])]
)
def test_longest_path_from(input, expected):
    adjacency = {
        "cat": {"at"},
        "bat": {"at"},
        "boy": {"by", "oy"},
        "oy": {"o"},
        "at": {"a"},
        "a": set(),
        "o": set(),
        "by": set(),
    }

    result = list(main.longest_paths_from(adjacency, input))
    assert result == expected


def test_longest_paths_from_each_origin():
    wordlist = ["cat", "bat", "boy", "oy", "at", "a", "o", "by"]
    result = list(main.longest_paths_from_each_origin(wordlist))
    expected = [
        ["cat", "at", "a"],
        ["bat", "at", "a"],
        ["boy", "oy", "o"],
        ["at", "a"],
        ["oy", "o"],
        ["a"],
        ["o"],
        ["by"],
    ]
    assert sorted(result) == sorted(expected)
