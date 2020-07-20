"""Python Package Index

This module provides directives and roles for referencing Python packages upon PyPI.

.. note ::

    The code herein is a bit of a slapdash affair and does not represent best practice.
"""
from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes # No Idea what this really does

def make_link_node(rawtext, app, package, release, options):
    """Creates a link to the Python Package Index

    :param rawtext: Text being replaced with link node.
    :param app: Sphinx application context
    :param type: Link type (issue, changeset, etc.)
    :param package: ID of the thing to link to
    :param options: Options dictionary passed to role func.
    """
    # Input checking
    try:
        print(__package__,__name__)
        print(app.config)
        print(dir(app.config))
        uri = "https://pypi.org/project/" # app.config.get("pypi_project_url", "https://pypi.org/project/")
        if not uri:
            raise AttributeError
    except AttributeError as error:
        raise ValueError('pypi_project_url configuration value is not set (%s)' % str(error))
    url = "{website}/{package}/{release}/".format(website=uri.rstrip('/'), package=package, release=release) if release and release != "latest" else "{website}/{package}".format(website=uri.rstrip('/'), package=package)
    set_classes(options)
    node = nodes.reference(rawtext, utils.unescape(package) + ":" + utils.unescape(release), refuri=url, **options)
    return node

def PyPI(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """The Python Package Index (PyPI) role

    The PyPI role replaces the provided package name and optionally the release/version, separated by a colon, into a hyperlink to the package upon the Python Package Index a.k.a. the Cheese Shop.

    :param name: The role name used in the document e.g. :ROLE:
    :param rawtext: The entire markup snippet, with role e.g. :ROLE:`TEXT`
    :param text: The text marked with the role e.g. `TEXT`
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    :return:
    """
    package = text
    # Should error checking be necessary
    # try:
    #     package = int(text)
    #     if package <= 0:
    #         raise ValueError
    # except ValueError:
    #     msg = inliner.reporter.error(
    #         'BitBucket issue number must be a number greater than or equal to 1; '
    #         '"%s" is invalid.' % text, line=lineno)
    #     prb = inliner.problematic(rawtext, rawtext, msg)
    #     return [prb], [msg]
    app = inliner.document.settings.env.app
    package, *_, release = package.split(":") + ["latest"]
    node = make_link_node(rawtext, app, package, release, options)
    return [node], []

def setup(app):
    app.add_role('pypi', PyPI)

    return {'version': '0.1'}
