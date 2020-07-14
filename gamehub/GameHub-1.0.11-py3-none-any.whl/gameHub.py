"""
An interface to play multiple games
"""
import random
import json
from pathlib import Path
from difflib import get_close_matches
from typing import Callable

from games import hangMan, ticTacToe, rockPaperScissors
from utils.logging import MyLogger


logger = MyLogger.logging.getLogger('gamehub.gamehub')
gamehub_directory = Path.home() / '.gameHub'

last_game_played: Callable
last_game: Callable

game_interpreter = {
    "tictactoe": ticTacToe.game,
    "hangman": hangMan.game,
    "rps": rockPaperScissors.game
}


def change_last_game(game: str) -> None:
    """
    changes the last game to the game just played
    :param game: the new last played game
    :return: nothing
    """
    config_file = gamehub_directory / 'lastGame.json'
    config = json.loads(config_file.read_text())
    config["lastGame"] = game

    with config_file.open(mode='w') as outfile:
        json.dump(config, outfile, indent=2)


def generate() -> Callable:
    """
    Pick Random Game to play
    :return: picked game
    """
    list_things = [rockPaperScissors.rps_game, hangMan.game, ticTacToe.game]
    picked_game = list_things[random.randint(0, 2)]
    game_changer = {
        rockPaperScissors.rps_game: "rps",
        ticTacToe.game: "tictactoe",
        hangMan.game: "hangman"
    }
    change_last_game(game_changer[picked_game])
    return picked_game


def play_random_game_from_list(games: iter) -> None:
    """
    play's a random game from a given list. if one of the games is spelt wrong it prints the closest matching command
    in case they misspell them.
    :param games: list of games to randomly chose from
    """
    for game in games:
        if game not in game_interpreter.keys():
            print(f"{game} is not an available game")
            closest_matching_command = get_close_matches(game, game_interpreter.keys())
            print(f"did you mean: {closest_matching_command}")
            return
    game_interpreter[random.choice(games)]()


def play_hang_man() -> None:
    """
    play Hang Man game
    """
    hangMan.game()
    change_last_game("hangman")


def play_rps() -> None:
    """
    Play Rock Paper Scissors
    """
    rockPaperScissors.game()
    change_last_game("rps")


def play_tic_tac_toe() -> None:
    """
    Play Tic Tac Toe
    """
    ticTacToe.game()
    change_last_game("tictactoe")


def play_again() -> None:
    """
    plays the last game you played
    """
    logger.info("Playing the last game")
    config_file = Path.home() / '.gameHub/lastGame.json'
    config = json.loads(config_file.read_text())
    game_interpreter[config["lastGame"]]()
