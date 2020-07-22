# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rusyll']

package_data = \
{'': ['*'], 'rusyll': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

entry_points = \
{'console_scripts': ['rusyll = rusyll.rusyll:main']}

setup_kwargs = {
    'name': 'rusyll',
    'version': '0.1.1',
    'description': 'Splitting Russian words into phonetic syllables',
    'long_description': '# rusyll\n Python 3 package for dividing Russian words into phonetic syllables.\n## About\nThis package provides algorithmic phonetic syllable division for Russian language, similar to [nltk SyllableTokenizer](https://github.com/nltk/nltk/blob/develop/nltk/tokenize/sonority_sequencing.py), but adding some language-specific rules.\n\nIn fact, there are no unified rules for breaking words into syllables in Russian. Therefore I\'ve selected the most applicable rule set developed by R. I. Avanesov, professor of MSU, in 50s. In short it\'s based on the sonority index of the letters.\n\nThis package can be useful for various Natural Language applications. However, it is not suitable for hyphenation.\n\n## Installation\n`pip install rusyll`\n\n\n## How to use\n\n```python\n>>> from rusyll import rusyll\n>>> rusyll.token_to_syllables("черепаха")\n[\'че\', \'ре\', \'па\', \'ха\']\n>>> rusyll.word_to_syllables("черепаха-гофер")\n[\'че\', \'ре\', \'па\', \'ха\', \'го\', \'фер\']\n>>> rusyll.word_to_syllables_wd("черепаха-гофер")\n[\'че\', \'ре\', \'па\', \'ха\', \'-\', \'го\', \'фер\']\n>>> rusyll.word_to_syllables_safe("черепаха гофер")\n>>> Traceback (most recent call last):\nFile "<stdin>", line 1, in <module>\nFile "/home/toor_2/wonder/Python/rusyll/src/rusyll/rusyll.py",\nline 125, in word_to_syllables_safe\nassert bool(AssertionError: Word contains unsuitable symbols\n>>> rusyll.word_to_syllables_safe("черепаха-гофер")\n[\'че\', \'ре\', \'па\', \'ха\', \'го\', \'фер\']\n>>> help(rusyll)\n#...complete description of functions\n```\n## Feedback\nThis is my first attempt to make proper package for PyPI, so any feedback is highly appreciated!\n',
    'author': 'Simon Weiss',
    'author_email': 'wonder@simonweiss.space',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/weiss-d/rusyll',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
