# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skranger', 'skranger.ensemble']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'scikit-learn']

setup_kwargs = {
    'name': 'skranger',
    'version': '0.1.1',
    'description': 'Python bindings for C++ ranger random forests',
    'long_description': 'skranger\n========\n\n``skranger`` provides `scikit-learn <https://scikit-learn.org/stable/index.html>`__ compatible Python bindings to the C++ random forest implementation, `ranger <https://github.com/imbs-hl/ranger>`__, using `Cython <https://cython.readthedocs.io/en/latest/>`__.\n\nThe latest release of ``skranger`` uses version `0.12.1 <https://github.com/imbs-hl/ranger/releases/tag/0.12.1>`__ of ``ranger``.\n\n\nInstallation\n------------\n\n``skranger`` is available on `pypi <https://pypi.org/project/skranger>`__ and can be installed via pip:\n\n.. code-block:: bash\n\n    pip install skranger\n\n\nUsage\n-----\n\nThere are two ``sklearn`` compatible classes, ``RangerForestClassifier`` and ``RangerForestRegressor``. There is also the ``RangerForestSurvival`` class, which aims to be compatible with the `scikit-survival <https://github.com/sebp/scikit-survival>`__ API.\n\n\nRangerForestClassifier\n~~~~~~~~~~~~~~~~~~~~~~\n\nThe ``RangerForestClassifier`` predictor uses ``ranger``\'s ForestProbability class to enable both ``predict`` and ``predict_proba`` methods.\n\n.. code-block:: python\n\n    from sklearn.datasets import load_iris\n    from sklearn.model_selection import train_test_split\n    from skranger.ensemble import RangerForestClassifier\n\n    X, y = load_iris(True)\n    X_train, X_test, y_train, y_test = train_test_split(X, y)\n\n    rfc = RangerForestClassifier()\n    rfc.fit(X_train, y_train)\n\n    predictions = rfc.predict(X_test)\n    print(predictions)\n    # [1 2 0 0 0 0 1 2 1 1 2 2 2 1 1 0 1 1 0 1 1 1 0 2 1 0 0 1 2 2 0 1 2 2 0 2 0 0]\n\n    probabilities = rfc.predict_proba(X_test)\n    print(probabilities)\n    # [[0.01333333 0.98666667 0.        ]\n    #  [0.         0.         1.        ]\n    #  ...\n    #  [0.98746032 0.01253968 0.        ]\n    #  [0.99       0.01       0.        ]]\n\n\nRangerForestRegressor\n~~~~~~~~~~~~~~~~~~~~~\n\nThe ``RangerForestRegressor`` predictor uses ``ranger``\'s ForestRegression class.\n\n.. code-block:: python\n\n    from sklearn.datasets import load_boston\n    from sklearn.model_selection import train_test_split\n    from skranger.ensemble import RangerForestRegressor\n\n    X, y = load_boston(True)\n    X_train, X_test, y_train, y_test = train_test_split(X, y)\n\n    rfr = RangerForestRegressor()\n    rfr.fit(X_train, y_train)\n\n    predictions = rfr.predict(X_test)\n    print(predictions)\n    # [20.01270808 24.65041667 11.97722067 20.10345    26.48676667 42.19045952\n    #  19.821      31.51163333  8.34169603 18.94511667 20.21901915 16.01440705\n    #  ...\n    #  18.37752952 19.34765    20.13355    21.19648333 18.91611667 15.58964837\n    #  31.4223    ]\n\n\nRangerForestSurvival\n~~~~~~~~~~~~~~~~~~~~\n\nThe ``RangerForestSurvival`` predictor uses ``ranger``\'s ForestSurvival class, and has an interface similar to the RandomSurvivalForest found in the ``scikit-survival`` package.\n\n.. code-block:: python\n\n    from sksurv.datasets import load_veterans_lung_cancer\n    from sklearn.model_selection import train_test_split\n    from skranger.ensemble import RangerForestSurvival\n\n    X, y = load_veterans_lung_cancer()\n    # select the numeric columns as features\n    X = X[["Age_in_years", "Karnofsky_score", "Months_from_Diagnosis"]]\n    X_train, X_test, y_train, y_test = train_test_split(X, y)\n\n    rfs = RangerForestSurvival()\n    rfs.fit(X_train, y_train)\n\n    predictions = rfs.predict(X_test)\n    print(predictions)\n    # [107.99634921  47.41235714  88.39933333  91.23566667  61.82104762\n    #   61.15052381  90.29888492  47.88706349  21.25111508  85.5768254\n    #   ...\n    #   56.85498016  53.98227381  48.88464683  95.58649206  48.9142619\n    #   57.68516667  71.96549206 101.79123016  58.95402381  98.36299206]\n\n    chf = rfs.predict_cumulative_hazard_function(X_test)\n    print(chf)\n    # [[0.04233333 0.0605     0.24305556 ... 1.6216627  1.6216627  1.6216627 ]\n    #  [0.00583333 0.00583333 0.00583333 ... 1.55410714 1.56410714 1.58410714]\n    #  ...\n    #  [0.12933333 0.14766667 0.14766667 ... 1.64342857 1.64342857 1.65342857]\n    #  [0.00983333 0.0112619  0.04815079 ... 1.79304365 1.79304365 1.79304365]]\n\n    survival = rfs.predict_survival_function(X_test)\n    print(survival)\n    # [[0.95855021 0.94129377 0.78422794 ... 0.19756993 0.19756993 0.19756993]\n    #  [0.99418365 0.99418365 0.99418365 ... 0.21137803 0.20927478 0.20513086]\n    #  ...\n    #  [0.87868102 0.86271864 0.86271864 ... 0.19331611 0.19331611 0.19139258]\n    #  [0.99021486 0.98880127 0.95299007 ... 0.16645277 0.16645277 0.16645277]]\n\n\nLicense\n-------\n\n``skranger`` is licensed under `GPLv3 <https://github.com/crflynn/skranger/blob/master/LICENSE.txt>`__.\n\nDevelopment\n-----------\n\nTo develop locally, it is recommended to have ``asdf``, ``make`` and a C++ compiler already installed. After cloning, run ``make setup``. This will setup the ranger submodule, install python and poetry from ``.tool-versions``, install dependencies using poetry, copy the ranger source code into skranger, and then build and install skranger in the local virtualenv.\n\nTo format code, run ``make fmt``. This will run isort and black against the .py files.\n\nTo run tests and inspect coverage, run ``make test``.\n\nTo rebuild in place after making changes, run ``make build``.\n\nTo create python package artifacts, run ``make dist``.\n\nTo build and view documentation, run ``make docs``.\n',
    'author': 'Flynn',
    'author_email': 'crf204@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/crflynn/skranger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
