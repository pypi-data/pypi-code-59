# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['seaborn_image']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib-scalebar>=0.6.2,<0.7.0',
 'matplotlib>=3.2.2,<4.0.0',
 'palettable>=3.3.0,<4.0.0',
 'scikit-image>=0.17.2,<0.18.0',
 'scipy>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'seaborn-image',
    'version': '0.1.0',
    'description': 'seaborn-image: image data visualization and processing like seaborrn using matplotlib, scipy and scikit-image',
    'long_description': '=======================================\nseaborn-image: image data visualization\n=======================================\n\n\nSeaborn like image data visualization using matplotlib, scikit-image and scipy.\n\n\nDescription\n===========\n\nSeaborn-image is a seaborn like python **image** visualization and processing library\nbased on matplotlib.\n\nThe aim of seaborn-image is to provide a high-level API to **plot attractive images quickly**\n**and effectively**.\n\n\nInstallation\n============\n\n``pip install seaborn-image``\n\nSimple usage\n\n.. code-block:: python\n\n    import seaborn_image as isns\n\n    """Set context like seaborn"""\n    isns.set_context("notbook")\n\n    """Plot publishable quality image in one line"""\n    isns.imgplot(data)\n\n    """Add a scalebar"""\n    isns.imgplot(data, scalebar=True, dx=1, units="um")\n\nApply image filters and plot\n\n.. code-block:: python\n\n    import seaborn_image as isns\n\n    isns.filterplot(data, filter="gaussian")\n\nNote\n====\n\nThis project was started because I was looking for a seaborn like library for images but couldn\'t find any.\nThe project is still a work in progress but give it a go and let me know...\n',
    'author': 'Sarthak Jariwala',
    'author_email': 'jariwala@uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SarthakJariwala/seaborn-image',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
