"""\
pytest config for sphinxcontrib/nosejob/tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note ::

    `tk0miya <https://github.com/sphinx-doc/sphinx/issues/7008#issuecomment-573092764>`_ provides instructions for setting up :mod:`sphinx.testing`
"""
import pytest
from sphinx.testing.path import path

pytest_plugins = 'sphinx.testing.fixtures'

@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'documents'
