"""
Games cli
"""
import click


from games import hangMan, rockPaperScissors, ticTacToe


@click.group('play', short_help='group of all games')
def cli() -> None:
    """Contains all games"""
    pass


@cli.command('hang', short_help='Plays Hangman game')
def hangman() -> None:
    """Plays Hangman game"""
    hangMan.game()


@cli.command('rps', short_help='Plays Rock Paper Scissors game')
def rps() -> None:
    """Plays rock paper scissors game"""
    rockPaperScissors.game()


@cli.command('tic', short_help='Plays Tic Tac Toe game')
def tictactoe() -> None:
    """Plays Tic tac toe game"""
    ticTacToe.game()
