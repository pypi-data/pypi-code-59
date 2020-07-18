# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moms_apriltag', 'moms_apriltag.bin', 'moms_apriltag.tags']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'opencv-python']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata']}

entry_points = \
{'console_scripts': ['apriltag_generator = moms_apriltag.bin.gen:main']}

setup_kwargs = {
    'name': 'moms-apriltag',
    'version': '0.0.1',
    'description': 'Generate apriltags',
    'long_description': '# Apriltag - still under development \n\nWhy? There didn\'t really seem to be an easy way to do this IMHO.\n\n## Install\n\n```\npip install apriltag_gen\n```\n\n## Example\n\n```\n#!/usr/bin/env python3\nimport apriltag_gen as apt\n\nif __name__ == \'__main__\':\n    family = "tag36h11"\n    a = 12\n    b = 22\n    tags = apt.generate(family, range(a,b))\n    apt.save("png", tags, 30)\n```\n\n# MIT License\n\n**Copyright (c) 2020 Kevin J. Walchko**\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/apriltag_gen/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
