# -*- coding: utf-8 -*-
# Copyright (c) 2008, 2010, 2013 LOGILAB S.A. (Paris, FRANCE) <contact@logilab.fr>
# Copyright (c) 2014-2018 Claudiu Popa <pcmanticore@gmail.com>
# Copyright (c) 2014 Google, Inc.
# Copyright (c) 2014 Arun Persaud <arun@nubati.net>
# Copyright (c) 2015 Ionel Cristian Maries <contact@ionelmc.ro>
# Copyright (c) 2016 Derek Gustafson <degustaf@gmail.com>
# Copyright (c) 2018 Ville Skyttä <ville.skytta@iki.fi>
# Copyright (c) 2019-2020 Pierre Sassoulas <pierre.sassoulas@gmail.com>
# Copyright (c) 2019 Ashley Whetter <ashley@awhetter.co.uk>
# Copyright (c) 2020 Anthony Sottile <asottile@umich.edu>

# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

"""
unit test for visitors.diadefs and extensions.diadefslib modules
"""


import codecs
import os
from difflib import unified_diff

import pytest

from pylint.pyreverse.diadefslib import DefaultDiadefGenerator, DiadefsHandler
from pylint.pyreverse.inspector import Linker, project_from_files
from pylint.pyreverse.utils import get_visibility
from pylint.pyreverse.writer import DotWriter

_DEFAULTS = {
    "all_ancestors": None,
    "show_associated": None,
    "module_names": None,
    "output_format": "dot",
    "diadefs_file": None,
    "quiet": 0,
    "show_ancestors": None,
    "classes": (),
    "all_associated": None,
    "mode": "PUB_ONLY",
    "show_builtin": False,
    "only_classnames": False,
}


class Config:
    """config object for tests"""

    def __init__(self):
        for attr, value in _DEFAULTS.items():
            setattr(self, attr, value)


def _file_lines(path):
    # we don't care about the actual encoding, but python3 forces us to pick one
    with codecs.open(path, encoding="latin1") as stream:
        lines = [
            line.strip()
            for line in stream.readlines()
            if (
                line.find("squeleton generated by ") == -1
                and not line.startswith('__revision__ = "$Id:')
            )
        ]
    return [line for line in lines if line]


def get_project(module, name="No Name"):
    """return an astroid project representation"""

    def _astroid_wrapper(func, modname):
        return func(modname)

    return project_from_files([module], _astroid_wrapper, project_name=name)


DOT_FILES = ["packages_No_Name.dot", "classes_No_Name.dot"]


@pytest.fixture(scope="module")
def setup():
    project = get_project(os.path.join(os.path.dirname(__file__), "data"))
    linker = Linker(project)
    CONFIG = Config()
    handler = DiadefsHandler(CONFIG)
    dd = DefaultDiadefGenerator(linker, handler).visit(project)
    for diagram in dd:
        diagram.extract_relationships()
    writer = DotWriter(CONFIG)
    writer.write(dd)
    yield
    for fname in DOT_FILES:
        try:
            os.remove(fname)
        except FileNotFoundError:
            continue


@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("generated_file", DOT_FILES)
def test_dot_files(generated_file):
    expected_file = os.path.join(os.path.dirname(__file__), "data", generated_file)
    generated = _file_lines(generated_file)
    expected = _file_lines(expected_file)
    generated = "\n".join(generated)
    expected = "\n".join(expected)
    files = "\n *** expected : %s, generated : %s \n" % (expected_file, generated_file)
    assert expected == generated, "%s%s" % (
        files,
        "\n".join(
            line for line in unified_diff(expected.splitlines(), generated.splitlines())
        ),
    )
    os.remove(generated_file)


@pytest.mark.parametrize(
    "names, expected",
    [
        (["__reduce_ex__", "__setattr__"], "special"),
        (["__g_", "____dsf", "__23_9"], "private"),
        (["simple"], "public"),
        (
            ["_", "__", "___", "____", "_____", "___e__", "_nextsimple", "_filter_it_"],
            "protected",
        ),
    ],
)
def test_get_visibility(names, expected):
    for name in names:
        got = get_visibility(name)
        assert got == expected, "got %s instead of %s for value %s" % (
            got,
            expected,
            name,
        )
