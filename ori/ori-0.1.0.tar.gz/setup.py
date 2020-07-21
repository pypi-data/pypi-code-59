# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ori']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ori',
    'version': '0.1.0',
    'description': 'Concurrency tools for Python.',
    'long_description': 'Ori, a high-level concurrency library for Python\n=================================================\n\nOri is a high-level wrapper around Python\'s `concurrent.futures` module, designed to make multithreading and multiprocessing as easy as possible.\n\n\nFrequently Asked Questions (FAQs)\n---------------------------------\n\n**Who made Ori?**\n\nOri was written by `James Mishra <https://jamesmishra.com>`_ and incubated at `Neocrym <https://neocrym.com>`_, a record label that uses artificial intelligence to find and promote musicians. Neocrym heavily relies on Ori to make their I/O-bound Python code run faster.\n\nThe source code for Ori is owned by Neocrym Records Inc, but licensed to Ori under the MIT License.\n\n**Why should I use Ori over directly interfacing with `concurrent.futures`?**\n\nThe Python module `concurrent.futures` was introduced as a high-level abstraction over lower-level interfaces like `threading.Thread` and `multiprocessing.Process`. However, `concurrent.futures` merely moves the problem away from managing threads or processes to managing *executors*. Ori has the ambitious goal of also abstracting away the executors--making multithreading or multiprocessing no harder than writing single-threaded code.\n\n**Is Ori a good replacement for Python\'s asyncio?**\n\nFor the hardcore `asyncio` user, probably not. Ori is focused on providing high-level abstractions over Python\'s `concurrent.futures` module that provides speed boosts for synchronous, I/O-bound Python.\n\n**Where did the name "Ori" come from?**\n\nThe name "Ori" is a reference to the god-like villains in the Stargate TV shows. There is no meaningful connection between the villains or concurrency.\n',
    'author': 'James Mishra',
    'author_email': 'james.mishra@neocrym.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
