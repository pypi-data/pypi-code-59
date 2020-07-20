import pytest
from bs4 import BeautifulSoup
import logging

# pytestmark = pytest.mark.sphinx('html', testroot='trees') # Example of a generic decorator, with module scope, that PyTest will apply to all tests

LOG = logging.getLogger(__name__)

@pytest.mark.sphinx(testroot="trees", buildername="html") # , confoverrides={"master_doc" : "trees"}
def test_html_trees(app, status, warning):
    app.build()
    LOG.info(app.outdir.listdir())
    path = (app.outdir / "index.html")
    with path.open("rt") as file:
        html = BeautifulSoup(file)
        tree = html.findAll(id="tree")
        assert tree


@pytest.mark.sphinx(testroot="trees", buildername="latex")
def test_LaTeX_trees(app, status, warning):
    app.build()
    LOG.info(app.outdir.listdir())
    file = (app.outdir/'index.tex')

