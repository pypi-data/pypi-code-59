"""
holds all commands
"""
import click
from click_repl import repl
from prompt_toolkit.history import FileHistory

import gameHub
from games import gameCLI

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli() -> None:
    """
    the group of all the commands
    """
    pass


@cli.command('generate', short_help="Pick Random Game to play")
def click_generate() -> None:
    """
    Pick Random Game to play
    """
    gameHub.generate()()


@cli.command("last_game", short_help="plays the last game you played")
def play_again() -> None:
    """plays the last game you played"""
    gameHub.play_again()


@cli.command("play_list", short_help="play's a random game from a list")
@click.option('--games', '-g', nargs=1, type=str, help="Games to pick from", multiple=True)
def play_from_list(games) -> None:
    """
    play's a random game from a list and prints the closest command if you misspell it.
    \f
    :param games: string will print
    """
    gameHub.play_random_game_from_list(games)


@cli.command('repl', short_help="creates a repl and a exit command")
def create_repl() -> None:
    """
    creates a repl and a exit command
    """
    @cli.command("exit", short_help="breaks you out of repl")
    def exit_repl() -> None:
        """
        breaks you out of repl
        """
        raise EOFError
    cli.add_command(exit_repl)
    command_history_file = gameHub.gamehub_directory / 'system/my_repl_history'
    command_history_file.parent.mkdir(parents=True, exist_ok=True)
    prompt_kwargs = {
        'history': FileHistory(command_history_file),
    }
    repl(click.get_current_context(), prompt_kwargs=prompt_kwargs)


cli.add_command(gameCLI.play)
