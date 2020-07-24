import codecs
import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


#####
# Helper functions
#####
def read(*filenames, **kwargs):
    """
    Build an absolute path from ``*filenames``, and  return contents of
    resulting file.  Defaults to UTF-8 encoding.
    """
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for fl in filenames:
        with codecs.open(os.path.join(HERE, fl), "rb", encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_requirements(filename):
    reqs_txt = read(filename)
    parsed = reqs_txt.split("\n")
    parsed = [r.split("==")[0] for r in parsed]
    return [r for r in parsed if len(r) > 0]


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="heroicli",
    url="https://github.com/sjoeboo/heroicli",
    author="sjoeboo",
    author_email="sjoeboo@sjoeboo.com",
    maintainer="sjoeboo",
    maintainer_email="sjoeboo@sjoeboo.com",
    description="A Cli for the Heroic TSDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=read_requirements("requirements.txt"),
    packages=["heroicli"],
    python_requires='>=3.6',
    entry_points={"console_scripts": ["heroicli=heroicli.cli:cli"]},
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
