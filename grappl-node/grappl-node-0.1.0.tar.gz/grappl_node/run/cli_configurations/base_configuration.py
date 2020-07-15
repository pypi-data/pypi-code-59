import click
from functools import wraps
from ..cli import execute_cli


def configuration(*argument_names):
    """
    Decorates a function which is meant to return the configuration options for the node running environment.
    Example:
    >>>
    @configuration('param_1', 'param_2')
    def from_params_1_and_2(param_1, param_2):
        return {'param_1': param_1, 'param_2': param_2}

    @configuration
    def from_null():
        return {}

    @configuration(['param_3', 'param_4'])
    def from_params_3_and_4(param_3, param_4):
        return {3: param_3, 4: param_4}
    <<<
    """
    if len(argument_names) == 1 and isinstance(argument_names[0], (list, tuple, set)):
        argument_names = list(argument_names[0])

    @wraps
    def _click_command(func):
        last_command = None
        for group_command in execute_cli.commands:
            if argument_names is not func:
                for argument_name in argument_names:
                    func = click.argument(argument_name)(func)
            last_command = group_command.command()(func)
        return last_command
    return _click_command if isinstance(argument_names[0], (list, str)) else _click_command(argument_names)
