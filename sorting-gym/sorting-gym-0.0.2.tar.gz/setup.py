# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sorting_gym', 'sorting_gym.agents', 'sorting_gym.envs']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.17.2,<0.18.0', 'numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'sorting-gym',
    'version': '0.0.2',
    'description': 'OpenAI Gym Environments for Sorting based',
    'long_description': '# Sorting Gym\n\nOpenAI Gym Environments for Sorting based on the 2020 paper\n[_Strong Generalization and Efficiency in Neural Programs_](https://arxiv.org/abs/2007.03629) by \n_Yujia Li, Felix Gimeno, Pushmeet Kohli, Oriol Vinyals_.\n\nThis repository includes implementations of the basic neural environment for sorting.\n\nInstall from pypi (recommended) with:\n```\npip install sorting-gym\n```\n\nEnvironments:\n\n- `SortTapeAlgorithmicEnv-v0`\n- `BasicNeuralSortInterfaceEnv-v0`\n\nIn the tests module we implement the manual agents from the paper.\n\nAgents may want to consider supporting parametric/auto-regressive actions:\n- https://docs.ray.io/en/master/rllib-models.html#autoregressive-action-distributions\n- https://arxiv.org/abs/1502.03509\n\n\n### Goals:\n\n- [x] Implement bubblesort/insertion sort environment.\n- [x] Implement bubblesort/insertion sort agents as tests.\n- [ ] Implement function stack environment\n- [ ] Implement quick sort agent to test function environment\n- [ ] Include an example solution to train an agent via RL\n- [ ] Environment rendering\n\n### Ideas to take it further:\n\n- [ ] Open PR to `gym` for a discrete parametric space\n- [ ] Abstract out a Neural Controller Mixin/Environment Wrapper?\n- [ ] Consider a different/enhanced instruction set.\n\n## Run test with pytest\n\n```\npytest\n```\n\n## Building/Packaging\n\n```\npoetry update\npoetry build\npoetry package\n```',
    'author': 'Brian Thorne',
    'author_email': 'brian@hardbyte.nz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hardbyte/sorting-gym',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)
