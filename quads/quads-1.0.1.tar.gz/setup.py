# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['quads']
setup_kwargs = {
    'name': 'quads',
    'version': '1.0.1',
    'description': 'A pure Python Quadtree implementation.',
    'long_description': '# `quads`\n\nA pure Python Quadtree implementation.\n\n[Quadtrees](https://en.wikipedia.org/wiki/Quadtree) are a useful data\nstructure for sparse datasets where the location/position of the data is\nimportant. They\'re especially good for spatial indexing & image processing.\n\nAn actual visualization of a `quads.QuadTree`:\n\n![quadtree_viz](docs/_static/quadtree_visualization.png)\n\n\n## Usage\n\n```python\n>>> import quads\n>>> tree = quads.QuadTree(\n...     (0, 0),  # The center point\n...     10,  # The width\n...     10,  # The height\n... )\n\n# You can choose to simply represent points that exist.\n>>> tree.insert((1, 2))\nTrue\n# ...or include extra data at those points.\n>>> tree.insert(quads.Point(4, -3, data="Samus"))\nTrue\n\n# You can search for a given point. It returns the point if found...\n>>> tree.find((1, 2))\nPoint(1, 2)\n\n# Or `None` if there\'s no match.\n>>> tree.find((4, -4))\nNone\n\n# You can also find all the points within a given region.\n>>> bb = quads.BoundingBox(min_x=-1, min_y=-2, max_x=2, max_y=2)\n>>> tree.within_bb(bb)\n[Point(1, 2)]\n\n# You can also search to find the nearest neighbors of a point, even\n# if that point doesn\'t have data within the quadtree.\n>>> tree.nearest_neighbors((0, 1), count=2)\n[\n    Point(1, 2),\n    Point(4, -4),\n]\n\n# And if you have `matplotlib` installed (not required!), you can visualize\n# the tree.\n>>> quads.visualize(tree)\n```\n\n\n## Installation\n\n```\n$ pip install quads\n```\n\n\n## Requirements\n\n* Python 3.7+ (untested on older versions but may work)\n\n\n## Running Tests\n\n```\n$ git clone https://github.com/toastdriven/quads.git\n$ cd quads\n$ poetry install\n$ poetry shell\n\n# Just the tests.\n$ pytest .\n\n# With coverage.\n$ pytest -s --cov=quads .\n# And with pretty reports.\n$ pytest -s --cov=quads . && coverage html\n```\n\n\n## License\n\nNew BSD\n',
    'author': 'Daniel Lindsley',
    'author_email': 'daniel@toastdriven.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/toastdriven/quads',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
