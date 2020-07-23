
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import RogueError
from .controllers.base import Base
from .controllers.project import Project
from .controllers.engine import Engine
from pathlib import Path
import os
import yaml

# configuration defaults
CONFIG = init_defaults('rogue', 'log.logging')
CONFIG['rogue']['url'] = 'https://dev.admin2.rogue.mutantcxo.com'
CONFIG['log.logging']['level'] = 'info'


class Rogue(App):
    """Rogue Cli primary application."""

    class Meta:
        label = 'rogue'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'json',
            'jinja2',
            'tabulate'
        ]

        # configuration handler
        config_handler = 'yaml'

        home = str(Path.home())
       
        if not os.path.isfile(f'{home}/.rogue.conf'):
            conf = {'rogue': {
                'token': '',
                 'url': 'https://dev.admin2.rogue.mutantcxo.com'
            }}

            with open(f'{home}/.rogue.conf', 'w') as outfile:
                yaml.dump(conf, stream=outfile, default_flow_style=False, indent=3)

        config_files = [
            '~/.rogue.conf'
        ]

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Project,
            Engine
        ]


class RogueTest(TestApp,Rogue):
    """A sub-class of Rogue that is better suited for testing."""

    class Meta:
        label = 'rogue'


def main():
    with Rogue() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except RogueError as e:
            print('RogueError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
