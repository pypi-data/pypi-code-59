import os
import importlib
import sys
import colorama

colorama.init()

os.chdir('./tests/')
sys.path.append('.')

for i in os.listdir('.'):
    if i not in ['__pycache__', 'test_runner.py', '__init__.py']:
        try:
            importlib.import_module(i[:-3]).tests.run()
        except AssertionError:
            print(colorama.Fore.RED, colorama.Back.LIGHTWHITE_EX, 'Failed a test in the file: ', i, colorama.Back.RESET, colorama.Fore.RESET)
            exit()