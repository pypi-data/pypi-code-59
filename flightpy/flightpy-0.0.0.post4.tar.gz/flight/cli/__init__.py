import sys
import click
from werkzeug.serving import run_simple
import os

CONFIG_DIR = (os.path.dirname(__file__))

class ConfigException(Exception):
  pass

# Create a click 'group' to contain our cli commands.
@click.group()
def cli():
  pass

def main():
    """ Flight CLI """
    try:
      cli()
    # TODO: add additional core exceptions here
    except ConfigException as config_error:
      print("CONFIG ERROR: " + str(config_error))
      sys.exit(1)
    except FileNotFoundError as FNF:
      print("CONFIG ERROR: " + str(FNF))
      sys.exit(1)
    except Exception as err:
        print("UNKNOWN ERROR: %s" % (str(err)))
        sys.exit(1)