# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['newtonpy']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'newtonpy',
    'version': '0.1.0',
    'description': 'A package to solve nonlinear equations',
    'long_description': '# NewtonPy\n\nA package to solve nonlinear equations by newtonpy–Raphson method\n\n## Exemple\n\n### One variable\n\nThe function:\n\n![Equation 1](docs/eq1.png)\n\n\nThe Jacobian of function:\n\n![Equation 2](docs/eq2.png)\n\n``` python\nimport newtonpy\nimport numpy as np\n\n(converged, error, solution) = newtonpy.solve(\n    lambda x: x ** 2,\n    lambda x: np.array([2 * x]),\n    x0=np.array([1.2]),\n    tol=0.001,\n    maxiter=100,\n)\nprint(solution)\n```\n\n### Multivariable\n\nThe function:\n\n![Equation 3](docs/eq3.png)\n\nThe Jacobian of function:\n\n![Equation 4](docs/eq4.png)\n\n\n``` python\nimport newtonpy\nimport numpy as np\n\n(converged, error, solution) = newtonpy.solve(\n    lambda x: np.array([x[0] ** 2 + x[1] ** 2, 2 * x[1]]),\n    lambda x: np.array([[2 * x[0], 2 * x[1]], [0, 2]]),\n    x0=np.array([1, 1]),\n    tol=1e-3,\n    maxiter=10,\n    verbose=True,\n)\nprint(solution)\n```\n\n\n## Documentation\n\n``` python\nimport newtonpy\nhelp(newtonpy)\n```\n\n\n## License and Copyright\n \nMIT License\n\nCopyright (c) 2020 Felipe M. S. Monteiro (<fmarkson@outlook.com>)\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n\n---\n\n\n\n\n\n\n',
    'author': 'Felipe M. S. Monteiro',
    'author_email': 'fmarkson@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/felipemarkson/newtonpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
