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


setup(
    name="heroicli",
    url="https://github.com/sjoeboo/heroicli",
    author="sjoeboo",
    author_email="sjoeboo@sjoeboo.com",
    maintainer="sjoeboo",
    maintainer_email="sjoeboo@sjoeboo.com",
    version="0.0.1",
    install_requires=read_requirements("requirements.txt"),
    packages=["heroicli"],
    entry_points={"console_scripts": ["heroicli=heroicli.cli:cli"]},
)
