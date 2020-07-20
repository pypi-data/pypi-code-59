# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oanda_chart', 'oanda_chart.env', 'oanda_chart.util', 'oanda_chart.widgets']

package_data = \
{'': ['*'], 'oanda_chart': ['image_data/*', 'workshop/*']}

install_requires = \
['forex-types>=0.0.6,<0.0.7',
 'oanda-candles>=0.0.6,<0.0.7',
 'tk-oddbox>=0.0.3,<0.0.4']

setup_kwargs = {
    'name': 'oanda-chart',
    'version': '0.0.3',
    'description': 'Oanda forex candle chart tkinter widget.',
    'long_description': '# oanda-chart\nOanda forex candle chart tkinter widget.\n\n#### Warning:\nThis package does not yet have all its core features, and even its\ncurrent features might change significantly.\n\nIt was uploaded to pypi.org early as an experiment to see if the package\ncould find some "png" after installation...not because it was at\nall ready.\n\n#### Some Background\nThis is being built on top of oanda-candles package which is built\non top of the oandaV20 package, which uses the Oanda Restful API.\n\nIt provides a tkinter chart widget and associated widgets to select\nthe instrument pair, granularity, and ask/mid/bid.\n\n\n\n\n\n',
    'author': 'Andrew Allaire',
    'author_email': 'andrew.allaire@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aallaire/oanda-chart',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
