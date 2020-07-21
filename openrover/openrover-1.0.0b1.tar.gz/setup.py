# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openrover', 'openrover.tests', 'openrover.tests.burnin']

package_data = \
{'': ['*'], 'openrover.tests': ['resources/*']}

install_requires = \
['async_generator>=1.10,<2.0',
 'booty>=0.3.0,<0.4.0',
 'pyserial>=3.4,<4.0',
 'pytest-trio>=0.6.0,<0.7.0',
 'pytest>=5.4.3,<6.0.0',
 'trio>=0.16.0,<0.17.0']

entry_points = \
{'console_scripts': ['openrover-tests = openrover:main',
                     'pitstop = openrover.pitstop:main']}

setup_kwargs = {
    'name': 'openrover',
    'version': '1.0.0b1',
    'description': 'A Python driver for driving the Rover Robotics OpenRover Basic robot',
    'long_description': '# OpenRover Python Suite\n\nThis is the official Python driver for the [Rover Robotics](https://roverrobotics.com/) "Open Rover Basic" robot. Use this as a starting point to get up and running quickly.\n\nIncluded in this package are:\n\n1. A Python library for programmatically interfacing with the Rover over USB\n2. A command line application "`pitstop`" for upgrading and configuring the Rover firmware\n3. A test suite that confirms the Firmware and hardware are operating as expected.\n\n## Setup\n\nTo install official releases from PyPi:\n\n```shell script\npython3 -m pip install -U pip setuptools\npython3 -m pip install -U openrover --no-cache-dir\n```\n\nOn Linux, you may not have permission to access USB devices. If this is the case, run the following then restart your computer:\n\n```shell script\nsudo usermod -a -G dialout $(whoami)\n```\n\n### Development setup\n\nManual Prerequisites:\n\n* Python3 (recommended to install Python3.6, Python3.7, and Python3.8)\n* [Poetry](https://python-poetry.org/docs/#installation) \n\nInstead, we recommend:\n\n```\ngit clone https://github.com/RoverRobotics/openrover-python.git\ncd openrover-python\npoetry install\n```\n\n#### Useful commands\n\nFor development testing, it is recommended to use `tox`, which can run tests on multiple Python interpreters.\n\n<dl>\n    <dt><code>pytest</code></dt>\n    <dd>Test on current Python interpreter</dd>\n    <dt><code>tox</code></dt>\n    <dd>Test on all supported Python minor versions</dd>\n    <dt><code>black .</code></dt>\n    <dd>Reformat code to a uniform style</dd>\n    <dt><code>githooks setup</code></dt>\n    <dd>Install git pre-commit hook to automatically run <code>black</code></dd>\n</dl>\n\n### Caveats\n\n* When running in PyCharm in debug mode, you will get a warning like "RuntimeWarning: You seem to already have a custom sys.excepthook handler installed ..." https://github.com/python-trio/trio/issues/1553\n* Note this is a pyproject (PEP-517) project so it will NOT work to `pip install --editable ...` for development. Instead use `poetry install` as above.\n\n\n### pitstop\n\nPitstop is a helper program to bootload your rover and set options. After installing the openrover package, you can invoke it with `pitstop` or `python3 -m openrover.pitstop`.\n\n```text\n> pitstop --help\n  usage: pitstop [-h] [-p port] action ...\n  \n  OpenRover companion utility to bootload robot and configure settings.\n  \n  positional arguments:\n    action\n      flash               write the given firmware hex file onto the rover\n      checkversion        Check the version of firmware installed\n      test                Run tests on the rover\n      update              Update rover persistent settings\n  \n  optional arguments:\n    -h, --help            show this help message and exit\n    -p port, --port port  Which device to use. If omitted, we will search for a possible rover device\n```\n\n### tests\n\nTo run tests, first attach the rover via breakout cable then run `pitstop test`.\nBy default, tests that involve running the motors will be skipped, since you may not want a rover ripping cables out of your computer. If you have made sure running the motors will not damage anything, these tests can be opted in with the flag `--motorok`.\n\n```text\n> pitstop test --motorok\nScanning for possible rover devices\nUsing device /dev/ttyUSB0\n========================== test session starts ============================\nplatform linux -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1\nrootdir: /home/dan/Documents/openrover-python/openrover\nplugins: trio-0.6.0\ncollected 73 items                                                                                                                                                                                           \n\ntests/test_bootloader.py .s                                                                                                                                                                            [  2%]\ntests/test_find_device.py .....                                                                                                                                                                        [  9%]\ntests/test_openrover_protocol.py ....                                                                                                                                                                  [ 15%]\ntests/test_rover.py ..................x.x.........x................Xxxx..........                                                                                                                      [ 98%]\ntests/burnin/test_burnin.py s                                                                                                                                                                          [100%]\n\n===== 64 passed, 2 skipped, 6 xfailed, 1 xpassed in 83.94s (0:01:23) =====\n```\n\n![OpenRover Basic](https://docs.roverrobotics.com/1-manuals/0-cover-photos/1-open-rover-basic-getting-started-vga.jpg)\n',
    'author': 'Dan Rose',
    'author_email': 'dan@digilabs.io',
    'maintainer': 'Dan Rose',
    'maintainer_email': 'dan@digilabs.io',
    'url': 'https://github.com/RoverRobotics/openrover_python_driver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
