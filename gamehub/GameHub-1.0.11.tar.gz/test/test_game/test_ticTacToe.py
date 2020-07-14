"""
tests the tic tac toe module
"""
import pytest

from games import ticTacToe


@pytest.mark.parametrize("board,expected",
                         [  # checks middle column for player 1
                             ({"top_left": "-", "top_mid": "x", "top_right": "-",
                               "mid_left": "-", "mid_mid": "x", "mid_right": "-",
                               "bot_left": "-", "bot_mid": "x", "bot_right": "-"}, "player 1"),
                             # checks right column for player 1
                             ({"top_left": "-", "top_mid": "-", "top_right": "x",
                               "mid_left": "-", "mid_mid": "-", "mid_right": "x",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "x"}, "player 1"),
                             # checks left column for player 1
                             ({"top_left": "x", "top_mid": "-", "top_right": "-",
                               "mid_left": "x", "mid_mid": "-", "mid_right": "-",
                               "bot_left": "x", "bot_mid": "-", "bot_right": "-"}, "player 1"),
                             # checks top row for player 1
                             ({"top_left": "x", "top_mid": "x", "top_right": "x",
                               "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 1"),
                             # checks middle row for player 1
                             ({"top_left": "-", "top_mid": "-", "top_right": "-",
                               "mid_left": "x", "mid_mid": "x", "mid_right": "x",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 1"),
                             # checks bottom row for player 1
                             ({"top_left": "-", "top_mid": "-", "top_right": "-",
                               "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                               "bot_left": "x", "bot_mid": "x", "bot_right": "x"}, "player 1"),
                             # checks bot-left to top-right diagonal for player 1
                             ({"top_left": "-", "top_mid": "-", "top_right": "x",
                               "mid_left": "-", "mid_mid": "x", "mid_right": "-",
                               "bot_left": "x", "bot_mid": "-", "bot_right": "-"}, "player 1"),
                             # checks top-left to bot-right diagonal for player 1
                             ({"top_left": "x", "top_mid": "-", "top_right": "-",
                               "mid_left": "-", "mid_mid": "x", "mid_right": "-",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "x"}, "player 1"),
                             # checks middle column for player 2
                             ({"top_left": "-", "top_mid": "o", "top_right": "-",
                               "mid_left": "-", "mid_mid": "o", "mid_right": "-",
                               "bot_left": "-", "bot_mid": "o", "bot_right": "-"}, "player 2"),
                             # checks right column for player 2
                             ({"top_left": "-", "top_mid": "-", "top_right": "o",
                               "mid_left": "-", "mid_mid": "-", "mid_right": "o",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "o"}, "player 2"),
                             # checks left column for player 2
                             ({"top_left": "o", "top_mid": "-", "top_right": "-",
                               "mid_left": "o", "mid_mid": "-", "mid_right": "-",
                               "bot_left": "o", "bot_mid": "-", "bot_right": "-"}, "player 2"),
                             # checks top row for player 2
                             ({"top_left": "o", "top_mid": "o", "top_right": "o",
                               "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 2"),
                             # checks middle row for player 2
                             ({"top_left": "-", "top_mid": "-", "top_right": "-",
                               "mid_left": "o", "mid_mid": "o", "mid_right": "o",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 2"),
                             # checks bottom row for player 2
                             ({"top_left": "-", "top_mid": "-", "top_right": "-",
                               "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                               "bot_left": "o", "bot_mid": "o", "bot_right": "o"}, "player 2"),
                             # checks bot-left to top-right diagonal for player 2
                             ({"top_left": "-", "top_mid": "-", "top_right": "o",
                               "mid_left": "-", "mid_mid": "o", "mid_right": "-",
                               "bot_left": "o", "bot_mid": "-", "bot_right": "-"}, "player 2"),
                             # checks top-left to bot-right diagonal for player 2
                             ({"top_left": "o", "top_mid": "-", "top_right": "-",
                               "mid_left": "-", "mid_mid": "o", "mid_right": "-",
                               "bot_left": "-", "bot_mid": "-", "bot_right": "o"}, "player 2"),
                             # checks for tie
                             ({"top_left": "o", "top_mid": "x", "top_right": "o",
                               "mid_left": "o", "mid_mid": "x", "mid_right": "o",
                               "bot_left": "x", "bot_mid": "o", "bot_right": "x"}, "tie"),
                             # checks for if the game is still going on
                             ({"top_left": "o", "top_mid": "x", "top_right": "-",
                               "mid_left": "o", "mid_mid": "x", "mid_right": "-",
                               "bot_left": "x", "bot_mid": "o", "bot_right": "-"}, "")

                         ])
def test_checker(board: dict, expected: str) -> None:
    """
    Testing all combinations of the board
    """
    print("Board:\n{}\n".format(board))
    actual_output = ticTacToe.check_state_of_game(board)
    assert actual_output == expected


@pytest.mark.parametrize("board, maximising_player, expected",
                         [({"top_left": "-", "top_mid": "x", "top_right": "x",
                            "mid_left": "x", "mid_mid": "-", "mid_right": "o",
                            "bot_left": "x", "bot_mid": "o", "bot_right": "o"}, False, 1),

                          ({"top_left": "x", "top_mid": "-", "top_right": "o",
                            "mid_left": "o", "mid_mid": "-", "mid_right": "x",
                            "bot_left": "x", "bot_mid": "x", "bot_right": "-"}, False, 0),

                          ({"top_left": "o", "top_mid": "-", "top_right": "x",
                            "mid_left": "x", "mid_mid": "-", "mid_right": "o",
                            "bot_left": "o", "bot_mid": "o", "bot_right": "-"}, False, -1)
                          ])
def test_mini_max(board: dict, maximising_player: bool, expected: int) -> None:
    """
    Testing all combinations of the board
    """

    actual_output = ticTacToe.mini_max(board, maximising_player)
    print(actual_output)
    print(expected)
    assert actual_output == expected


@pytest.mark.parametrize("board, player_going_first, ai_move, expected",
                         # 1 / board0 - Player 1 - attacking------------------------------------------------------------

                         [({"top_left": "-", "top_mid": "-", "top_right": "/",
                            "mid_left": "x", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "x", "bot_mid": "/", "bot_right": "/"}, "player 1", "win", 0),
                          # 2 / board1
                          ({"top_left": "/", "top_mid": "-", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "x", "bot_right": "/"}, "player 1", "win", 1),
                          # 3 / board2
                          ({"top_left": "-", "top_mid": "/", "top_right": "-",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "x"}, "player 1", "win", 2),
                          # 4 / board3
                          ({"top_left": "-", "top_mid": "x", "top_right": "x",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "-", "bot_right": "/"}, "player 1", "win", 0),
                          # 5 / board4
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "-", "mid_mid": "x", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 1", "win", 3),
                          # 6 / board5
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "x", "bot_right": "x"}, "player 1", "win", 6),
                          # 7 / board6
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "-", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "x"}, "player 1", "win", 0),
                          # 8 / board7
                          ({"top_left": "/", "top_mid": "/", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "/", "bot_right": "/"}, "player 1", "win", 2),
                          # 9 / board8
                          ({"top_left": "/", "top_mid": "x", "top_right": "/",
                            "mid_left": "-", "mid_mid": "-", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "x", "bot_right": "/"}, "player 1", "win", 4),

                          # 1 / board9 - Player 2 - Blocking -----------------------------------------------------------

                          ({"top_left": "x", "top_mid": "/", "top_right": "/",
                            "mid_left": "x", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "/", "bot_right": "-"}, "player 2", "win", 6),
                          # 2 / board10
                          ({"top_left": "/", "top_mid": "x", "top_right": "/",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "-", "bot_right": "-"}, "player 2", "win", 7),
                          # 3 / board12
                          ({"top_left": "/", "top_mid": "/", "top_right": "x",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "-"}, "player 2", "win", 8),
                          # 4 / board13
                          ({"top_left": "x", "top_mid": "x", "top_right": "-",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "-",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 2", "win", 2),
                          # 5 / board14
                          ({"top_left": "/", "top_mid": "/", "top_right": "-",
                            "mid_left": "x", "mid_mid": "x", "mid_right": "-",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 2", "win", 5),
                          # 6 / board15
                          ({"top_left": "/", "top_mid": "/", "top_right": "/",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "x", "bot_right": "-"}, "player 2", "win", 8),
                          # 7 / board16
                          ({"top_left": "x", "top_mid": "/", "top_right": "/",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "-", "bot_right": "-"}, "player 2", "win", 8),
                          # 8 / board17
                          ({"top_left": "/", "top_mid": "-", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "x", "bot_mid": "/", "bot_right": "/"}, "player 2", "win", 2),
                          # 9 / board18
                          ({"top_left": "/", "top_mid": "-", "top_right": "/",
                            "mid_left": "x", "mid_mid": "-", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 1", "win", 4),

                          # 1 / board19 - DRAW - Player 1 --------------------------------------------------------------

                          ({"top_left": "-", "top_mid": "-", "top_right": "/",
                            "mid_left": "x", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "x", "bot_mid": "/", "bot_right": "/"}, "player 1", "draw", 1),
                          # 2 / board20
                          ({"top_left": "/", "top_mid": "-", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "x", "bot_right": "/"}, "player 1", "draw", 2),
                          # 3 / board21
                          ({"top_left": "-", "top_mid": "/", "top_right": "-",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "x"}, "player 1", "draw", 0),
                          # 4 / board22
                          ({"top_left": "-", "top_mid": "x", "top_right": "x",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "-", "bot_right": "/"}, "player 1", "draw", 7),
                          # 5 / board23
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "-", "mid_mid": "x", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 1", "draw", 0),
                          # 6 / board24
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "x", "bot_right": "x"}, "player 1", "draw", 0),
                          # 7 / board25
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "-", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "x"}, "player 1", "draw", 3),
                          # 8 / board26
                          ({"top_left": "/", "top_mid": "/", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "/", "bot_right": "/"}, "player 1", "draw", 5),
                          # 9 / board27
                          ({"top_left": "o", "top_mid": "x", "top_right": "/",
                            "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                            "bot_left": "o", "bot_mid": "x", "bot_right": "/"}, "player 1", "draw", 3),
                          # temporary
                          ({"top_left": "o", "top_mid": "o", "top_right": "-",
                            "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                            "bot_left": "-", "bot_mid": "-", "bot_right": "x"}, "player 1", "draw", 2),

                          # 1 / board28 - Player 2 - Blocking ----------------------------------------------------------

                          ({"top_left": "x", "top_mid": "/", "top_right": "/",
                            "mid_left": "x", "mid_mid": "/", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "/", "bot_right": "-"}, "player 2", "draw", 6),
                          # 2 / board29
                          ({"top_left": "/", "top_mid": "x", "top_right": "/",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "-", "bot_right": "-"}, "player 2", "draw", 7),
                          # 3 / board30
                          ({"top_left": "/", "top_mid": "/", "top_right": "x",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "x",
                            "bot_left": "-", "bot_mid": "/", "bot_right": "-"}, "player 2", "draw", 8),
                          # 4 / board31
                          ({"top_left": "x", "top_mid": "x", "top_right": "-",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "-",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 2", "draw", 2),
                          # 5 / board32
                          ({"top_left": "/", "top_mid": "/", "top_right": "-",
                            "mid_left": "x", "mid_mid": "x", "mid_right": "-",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 2", "draw", 5),
                          # 6 / board33
                          ({"top_left": "/", "top_mid": "/", "top_right": "/",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "x", "bot_right": "-"}, "player 2", "draw", 8),
                          # 7 / board34
                          ({"top_left": "x", "top_mid": "/", "top_right": "/",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "/", "bot_mid": "-", "bot_right": "-"}, "player 2", "draw", 8),
                          # 8 / board35
                          ({"top_left": "/", "top_mid": "-", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "x", "bot_mid": "/", "bot_right": "/"}, "player 2", "draw", 2),
                          # 9 / board36
                          ({"top_left": "/", "top_mid": "-", "top_right": "/",
                            "mid_left": "x", "mid_mid": "-", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "/"}, "player 2", "draw", 4),
                          # temporary
                          ({"top_left": "o", "top_mid": "o", "top_right": "-",
                            "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                            "bot_left": "-", "bot_mid": "-", "bot_right": "x"}, "player 2", "draw", 2),

                          # 1 / board37 - LOSE - player 1 - Attacking --------------------------------------------------

                          ({"top_left": "-", "top_mid": "-", "top_right": "-",
                            "mid_left": "o", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "o", "bot_mid": "x", "bot_right": "/"}, "player 1", "lose", 2),
                          # 2 / board38
                          ({"top_left": "-", "top_mid": "-", "top_right": "-",
                            "mid_left": "/", "mid_mid": "o", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "o", "bot_right": "x"}, "player 1", "lose", 0),
                          # 3 / board39
                          ({"top_left": "-", "top_mid": "-", "top_right": "-",
                            "mid_left": "/", "mid_mid": "x", "mid_right": "o",
                            "bot_left": "/", "bot_mid": "x", "bot_right": "o"}, "player 1", "lose", 0),
                          # 4 / board41
                          ({"top_left": "-", "top_mid": "o", "top_right": "o",
                            "mid_left": "-", "mid_mid": "x", "mid_right": "x",
                            "bot_left": "-", "bot_mid": "/", "bot_right": "/"}, "player 1", "lose", 6),
                          # 5 / board42
                          ({"top_left": "-", "top_mid": "x", "top_right": "x",
                            "mid_left": "-", "mid_mid": "o", "mid_right": "o",
                            "bot_left": "-", "bot_mid": "/", "bot_right": "/"}, "player 1", "lose", 6),
                          # 6 / board43
                          ({"top_left": "-", "top_mid": "/", "top_right": "/",
                            "mid_left": "-", "mid_mid": "x", "mid_right": "x",
                            "bot_left": "-", "bot_mid": "o", "bot_right": "o"}, "player 1", "lose", 0),
                          # 7 / board44
                          ({"top_left": "-", "top_mid": "x", "top_right": "x",
                            "mid_left": "/", "mid_mid": "o", "mid_right": "-",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "o"}, "player 1", "lose", 5),
                          # 8 / board45
                          ({"top_left": "x", "top_mid": "x", "top_right": "-",
                            "mid_left": "-", "mid_mid": "o", "mid_right": "/",
                            "bot_left": "o", "bot_mid": "/", "bot_right": "/"}, "player 1", "lose", 3),
                          # 9 / board46
                          ({"top_left": "/", "top_mid": "-", "top_right": "/",
                            "mid_left": "o", "mid_mid": "-", "mid_right": "o",
                            "bot_left": "x", "bot_mid": "-", "bot_right": "x"}, "player 1", "lose", 1),

                          # 1 / board47 - Player 2 - Blocking ----------------------------------------------------------

                          ({"top_left": "o", "top_mid": "x", "top_right": "/",
                            "mid_left": "o", "mid_mid": "x", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 2", "lose", 8),
                          # 2 / board48
                          ({"top_left": "x", "top_mid": "o", "top_right": "/",
                            "mid_left": "x", "mid_mid": "o", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 2", "lose", 8),
                          # 3 / board49
                          ({"top_left": "x", "top_mid": "/", "top_right": "o",
                            "mid_left": "x", "mid_mid": "/", "mid_right": "o",
                            "bot_left": "-", "bot_mid": "-", "bot_right": "-"}, "player 2", "lose", 7),
                          # 4 / board50
                          ({"top_left": "o", "top_mid": "o", "top_right": "-",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "x", "bot_right": "-"}, "player 2", "lose", 5),
                          # 5 / board51
                          ({"top_left": "/", "top_mid": "/", "top_right": "-",
                            "mid_left": "o", "mid_mid": "o", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "x", "bot_right": "-"}, "player 2", "lose", 2),
                          # 6 / board52
                          ({"top_left": "x", "top_mid": "x", "top_right": "-",
                            "mid_left": "/", "mid_mid": "/", "mid_right": "-",
                            "bot_left": "o", "bot_mid": "o", "bot_right": "-"}, "player 2", "lose", 5),
                          # 7 / board53
                          ({"top_left": "o", "top_mid": "-", "top_right": "x",
                            "mid_left": "/", "mid_mid": "o", "mid_right": "x",
                            "bot_left": "/", "bot_mid": "/", "bot_right": "-"}, "player 2", "lose", 1),
                          # 8 / board54
                          ({"top_left": "x", "top_mid": "-", "top_right": "o",
                            "mid_left": "x", "mid_mid": "o", "mid_right": "/",
                            "bot_left": "-", "bot_mid": "/", "bot_right": "/"}, "player 2", "lose", 1),
                          # 9 / board55
                          ({"top_left": "x", "top_mid": "o", "top_right": "/",
                            "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                            "bot_left": "x", "bot_mid": "o", "bot_right": "/"}, "player 2", "lose", 5),
                          ])
def test_best_move_for_ai(board: dict, player_going_first: str, ai_move: str, expected: int) -> None:
    """
    testing function best move for ai
    """
    actual_output = ticTacToe.best_move_for_ai(board, player_going_first, ai_move)
    assert actual_output == expected
