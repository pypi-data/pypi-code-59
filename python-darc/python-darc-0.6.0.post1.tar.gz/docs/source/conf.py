# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'darc'
copyright = '2019-2020, Jarry Shaw'
author = 'Jarry Shaw'

# The full version, including alpha/beta/rc tags
release = '0.6.0.post1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 'sphinx.ext.autodoc.typehints',
    'sphinxcontrib.napoleon',
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),

    'requests': ('https://requests.readthedocs.io/en/latest/', None),
    'selenium': ('https://www.selenium.dev/selenium/docs/api/py/', None),
    'stem': ('https://stem.torproject.org/', None),
}

autodoc_default_options = {
    'members': True,
    'member-order': 'groupwise',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__, _abc_impl, _unbound_fields, _wtforms_meta, _meta, _schema',
    'ignore-module-all': True,
    'private-members': True,
}
autodoc_typehints = 'description'
# autodoc_member_order = 'bysource'
# autodoc_member_order = 'alphabetic'

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None

manpages_url = 'https://linux.die.net/man/{section}/{page}'

do_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Customised hooks --------------------------------------------------------

import os

os.environ['TOR_PASS'] = 'null'


def maybe_skip_member(app, what: str, name: str, obj: object, skip: bool, options: dict):
    if name == '_abc_impl':
        return True
    if name == '__init__':
        if '__create_fn__' in obj.__qualname__:
            return True
    return skip


def remove_module_docstring(app, what: str, name: str, obj: object, options: dict, lines: list):
    if what == "module" and "darc" in name:
        lines.clear()


def setup(app):
    #app.connect("autodoc-process-docstring", remove_module_docstring)
    app.connect('autodoc-skip-member', maybe_skip_member)
