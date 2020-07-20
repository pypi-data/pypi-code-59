# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bibtexgen']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.0,<5.0.0',
 'requests>=2.23.0,<3.0.0',
 'tqdm>=4.45.0,<5.0.0']

entry_points = \
{'console_scripts': ['bibtexgen = bibtexgen.entry:main']}

setup_kwargs = {
    'name': 'bibtexgen',
    'version': '0.0.2',
    'description': 'A tool to quickly export all references to bibtex',
    'long_description': "# BibtexGen\n\n\n[![PyPi Version](https://img.shields.io/pypi/v/bibtexgen.svg)](https://pypi.org/project/bibtexgen/)\n[![PyPi License](https://img.shields.io/pypi/l/bibtexgen.svg)](https://pypi.org/project/bibtexgen/)\n[![PyPi PyVersions](https://img.shields.io/pypi/pyversions/bibtexgen.svg)](https://pypi.org/project/bibtexgen/)\n[![PyPi Format](https://img.shields.io/pypi/format/bibtexgen.svg)](https://pypi.org/project/bibtexgen/)\n\n| Continuous Integration | Continuous Delivery |\n|:--------:|:-----:|\n| ![test](https://github.com/sdabhi23/bibtexgen/workflows/test/badge.svg) | ![publish to pypi](https://github.com/sdabhi23/bibtexgen/workflows/publish%20to%20pypi/badge.svg) |\n\nA simple cli tool to generate a list of references of any paper available on Semantic Scholar as a .bib file.\n\n## Installation\n\nThis package supports only Python 3.5 and above.\n\n```bash\n$ pip install bibtexgen\n    Installing build dependencies ... done\n    Getting requirements to build wheel ... done\n        Preparing wheel metadata ... done\n.\n.\n.\nSuccessfully built bibtexgen\nInstalling collected packages: bibtexgen\nSuccessfully installed bibtexgen-0.0.1\n```\n\n## Usage\n\n* As cli tool:\n\n    ```bash\n    $ bibtexgen\n\n\n    ================================= Welcome to BibTex Generator =================================\n\n\n    Please enter the Sematic Scholar Id of your paper: 6258b37b8d517f121c844ebad226da472761adc6\n\n    Creating file 6258b37b8d517f121c844ebad226da472761adc6_references.bib\n\n    100%|█████████████████████████████████████████████████████████| 8/8 [00:21<00:00,  2.63s/papers]\n\n    Your references have been saved!\n    ```\n\n* Programmatically:\n\n    ```python\n    from bibtexgen import bibtex\n    from pprint import pprint\n\n    b = bibtex()\n    r = b.generate_references('6258b37b8d517f121c844ebad226da472761adc6')\n\n    pprint(r)\n    ```\n",
    'author': 'Shrey Dabhi',
    'author_email': 'shrey.dabhi23@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdabhi23/bibtexgen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
