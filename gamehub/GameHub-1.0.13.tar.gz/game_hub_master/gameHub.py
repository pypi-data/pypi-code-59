"""
An interface to play multiple games
"""
import random
import json
from pathlib import Path
from difflib import get_close_matches
from typing import Callable

from games import hangMan, ticTacToe, rockPaperScissors
from games.gameCLI import change_last_game
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


def play_again() -> None:
    """
    plays the last game you played
    """
    logger.info("Playing the last game")
    config_file = Path.home() / '.gameHub/lastGame.json'
    try:
        config = json.loads(config_file.read_text())
        logger.info(config['last_game'])
        if not config["last_game"]:
            logger.info("you haven't played a game yet")
        else:
            game_interpreter[config["last_game"]]()
    except FileNotFoundError:
        logger.warning("you haven't played a game yet")
