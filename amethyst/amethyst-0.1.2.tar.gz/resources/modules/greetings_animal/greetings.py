#!/usr/bin/env python3

"""
A test Amethyst output module used for demonstration purposes.
Usage:
modules/greetings_animal/animals.py | amethyst - | ./modules/greetings_animal/greetings.py
"""

import sys
import json
import os.path as op

ANIMALS_JSON_PATH = op.join(op.dirname(op.abspath(__file__)), 'animals.json')
with open(ANIMALS_JSON_PATH) as json_file:
    ENTRIES = json.load(json_file)

if len(sys.argv) != 1:
    print('Usage:')
    print('modules/greetings_animal/animals.py | amethyst - | modules/greetings_animal/greetings.py')
    sys.exit(1)

try:
    print('Hello %s!' % ENTRIES['gems'][sys.stdin.read().strip()]['label'])
except KeyError:
    print("stdin must be a gem identifier ('W', 'NW', 'N', 'NE', 'E', 'SE', 'S' or 'SW').")
