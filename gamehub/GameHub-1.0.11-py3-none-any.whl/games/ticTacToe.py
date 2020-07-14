"""
this is the tic tac toe game
"""
import random


from utils import inputHandlers
from utils.logging import MyLogger


logger = MyLogger.logging.getLogger('gamehub.games.hangMan')
list_of_slots = ["top_left", "top_mid", "top_right", "mid_left", "mid_mid", "mid_right",
                 "bot_left", "bot_mid", "bot_right"]
list_of_players = ["player 1", "player 2"]


def check_state_of_game(board: dict) -> str:
    """
    takes in a board as a dictionary and a list and then uses them to check who is the winner, loser or if it is a tie
    or the game hasn't finished yet.
    :param board: dictionary of all slots on the game board
    :return: the winning player, a tie or an empty string if the game is not finished
    """
    who_won = ""

    if board[list_of_slots[0]] == board[list_of_slots[1]] == board[list_of_slots[2]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[3]] == board[list_of_slots[4]] == board[list_of_slots[5]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[6]] == board[list_of_slots[7]] == board[list_of_slots[8]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[0]] == board[list_of_slots[3]] == board[list_of_slots[6]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[1]] == board[list_of_slots[4]] == board[list_of_slots[7]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[2]] == board[list_of_slots[5]] == board[list_of_slots[8]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[0]] == board[list_of_slots[4]] == board[list_of_slots[8]] == "x":
        who_won = "player 1"

    elif board[list_of_slots[2]] == board[list_of_slots[4]] == board[list_of_slots[6]] == "x":
        who_won = "player 1"

    if board[list_of_slots[0]] == board[list_of_slots[1]] == board[list_of_slots[2]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[3]] == board[list_of_slots[4]] == board[list_of_slots[5]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[6]] == board[list_of_slots[7]] == board[list_of_slots[8]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[0]] == board[list_of_slots[3]] == board[list_of_slots[6]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[1]] == board[list_of_slots[4]] == board[list_of_slots[7]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[2]] == board[list_of_slots[5]] == board[list_of_slots[8]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[0]] == board[list_of_slots[4]] == board[list_of_slots[8]] == "o":
        who_won = "player 2"

    elif board[list_of_slots[2]] == board[list_of_slots[4]] == board[list_of_slots[6]] == "o":
        who_won = "player 2"

    if who_won == "":
        for key, value in board.items():
            if value == "-":
                return ""
        return "tie"
    return who_won


def best_move_for_ai(board: dict, which_player_has_the_turn: str, ai_move: str) -> int:
    """
    using the mini_max function, it loops through all the moves for this turn and then finds out the best one by calling
    mini_max, and dependant on who's turn it is, the computer either saves the best score by looking for the lowest
    score (meaning player two's best move) or the highest score (meaning player one's best move)
    :param ai_move: does a thing
    :param board: the game board
    :param which_player_has_the_turn: who has the turn
    """
    logger.info(ai_move)
    let_board = board
    if which_player_has_the_turn == "player 1":
        maximising_player = False
        symbol_to_put_in_slot = "x"
    else:
        maximising_player = True
        symbol_to_put_in_slot = "o"
    best_move = float("-inf")
    mini_best_score = float("-inf")
    max_best_score = float("inf")
    while best_move == float("-inf"):
        for i in range(9):
            if let_board[list_of_slots[i]] == '-':
                let_board[list_of_slots[i]] = symbol_to_put_in_slot
                score = mini_max(let_board, maximising_player)
                if ai_move == "win":
                    if score > mini_best_score and not maximising_player:
                        mini_best_score = score
                        best_move = i
                    if score < max_best_score and maximising_player:
                        max_best_score = score
                        best_move = i
                if ai_move == "draw":
                    if score == 0 and not maximising_player:
                        mini_best_score = score
                        best_move = i
                    if -1 < score < max_best_score and maximising_player:
                        max_best_score = score
                        best_move = i
                if ai_move == "lose":
                    if score == -1 and not maximising_player:
                        mini_best_score = score
                        best_move = i
                    if score == 1 and maximising_player:
                        mini_best_score = score
                        best_move = i
                let_board[list_of_slots[i]] = "-"
        if ai_move == "draw":
            ai_move = "win"
        if ai_move == "lose":
            ai_move = "draw"
    return best_move


def mini_max(board: dict, maximizing_player: bool) -> int:
    """
    Given a board and the maximising player, it loops through the board, checks for an empty space, and if there
    is then it puts x into it and then calls itself, the function calls itself but switches the maximising player, so it
    then puts an o into the space, this keeps on going till the board is completed and it gets an evaluation of who won,
    this is then compared to the worst score (-infinity) and if it's better then it's replaced by the new evaluation. it
    goes on to the next possible ending and then compares that to the current score and if it's better replaces it. this
    keeps on going till all endings are done and the best ending is saved, then you go one up and then check the next
    branch in the tree. It then checks all these branches, gets the best branch and goes up again, and repeats until it
    get's back to the top.

    :param board: dictionary containing all the places to play
    :param maximizing_player: dependant of the bool passed in, it start the function on the maximising player ("x") or
    minimising player ("o")
    :return: whether or not the maximising or minimising player is going to win, draw or lose in the form of
    1 -> win | 0 -> draw | -1 -> lose
    """
    potential_scores = {"player 1": 1, "tie": 0, "player 2": -1}

    if check_state_of_game(board) != "":
        return potential_scores[check_state_of_game(board)]

    if maximizing_player:
        max_best_move = float('-inf')
        for i in range(9):
            if board[list_of_slots[i]] == '-':
                board[list_of_slots[i]] = "x"
                score = mini_max(board, False)
                board[list_of_slots[i]] = "-"
                if score > max_best_move:
                    max_best_move = score
        return max_best_move
    else:
        min_best_move = float('inf')
        for i in range(9):
            if board[list_of_slots[i]] == '-':
                board[list_of_slots[i]] = "o"
                score = mini_max(board, True)
                board[list_of_slots[i]] = "-"
                if score < min_best_move:
                    min_best_move = score
        return min_best_move


def print_board(board: dict):
    """
    saves the three rows of the tic, tac toe board and into separate variables and then prints them with a space between
    each board
    :return: nothing
    """
    return f"""
    {board['top_left']}  {board['top_mid']}  {board['top_right']}
    {board['mid_left']}  {board['mid_mid']}  {board['mid_right']}
    {board['bot_left']}  {board['bot_mid']}  {board['bot_right']}
    """


def tutorial() -> None:
    """
    tells players rules of the game
    :return: nothing
    """
    how_to_play = input("if you want to see the tutorial, type in [Y]es, if not - [N]o\n> ")
    while inputHandlers.check_for_bad_input_strings(how_to_play):
        how_to_play = input()
    how_to_play = how_to_play[0].upper()
    if how_to_play == 'Y':
        logger.info("""
    You pick the slot you want to pick using a number e.g

    -  -  -
    -  -  -
    -  -  -

    Is this:

    1  2  3
    4  5  6
    7  8  9

    To win get three in a row

    Here we'll show an example game so you don't screw up

    Player one it's your turn!

    Player one: 3

    -  -  x
    -  -  -
    -  -  -

    Player 2 it's your turn!

    Player 2: 6

    -  -  x
    -  -  o
    -  -  -

    ...And so on until one of the players get's three in a row

        """)


class TicTacToe:
    """
    holds the game code
    """

    def __init__(self) -> None:
        self.player_who_has_turn = ""
        self.dic_board = {"top_left": "-", "top_mid": "-", "top_right": "-",
                          "mid_left": "-", "mid_mid": "-", "mid_right": "-",
                          "bot_left": "-", "bot_mid": "-", "bot_right": "-"}
        self.top_row = f"{self.dic_board['top_left']}  {self.dic_board['top_mid']}  {self.dic_board['top_right']}"
        self.mid_row = f"{self.dic_board['mid_left']}  {self.dic_board['mid_mid']}  {self.dic_board['mid_right']}"
        self.bot_row = f"{self.dic_board['bot_left']}  {self.dic_board['bot_mid']}  {self.dic_board['bot_right']}"
        self.end_state_of_game = ""
        self.list_picked_slots = []
        self.list_ai_move_types = []

    def tictactoe_game(self) -> None:
        """
        checks if any one has one yet and if they have then return who is the winner, if no one has won then
        it picks the player who is going first, prints the board, asks the user to pick a slot and replaces the slot
        with the user's mark (x or o). After that, it checks if there is a tie (if so it breaks the loop) and if there
        isn't then it continues until the match has finished. Finally after the loop breaks it checks who won and then
        prints the winner.
        :return: who is the winner
        """
        tutorial()
        logger.info("(---------------------------- This is the actual game ----------------------------)")

        human_or_ai = input("do you want to play with a [H]uman or an [A]i\n> ")
        while True:
            while inputHandlers.check_for_bad_input_strings(human_or_ai):
                human_or_ai = input("> ")
            human_or_ai = human_or_ai[0].upper()
            if human_or_ai == "H" or human_or_ai == "A":
                break
            human_or_ai = input("you need to type in either [H]uman or [A]i\n> ")

        if human_or_ai == "H":
            self.player_who_has_turn = random.choice(list_of_players)
        else:
            self.player_who_has_turn = "player 2"

            break_loop = False
            while True:
                user_mode = input("do you want to play on [E]asy, [M]edium or [H]ard mode "
                                  "or make a [C]ustom difficulty?\n> ")
                while inputHandlers.check_for_bad_input_strings(user_mode):
                    user_mode = input("> ")
                user_mode = user_mode[0].upper()
                for i in ["H", "M", "E", "C"]:
                    if i == user_mode:
                        break_loop = True
                if break_loop:
                    break
                logger.info("Please enter either [E]asy, [M]edium, [H]ard or [C]ustom difficulty")
            freq_lose = 2
            freq_draw = 6
            freq_win = 6
            if user_mode == "H":
                freq_lose = 1
                freq_draw = 0
                freq_win = 16
            elif user_mode == "M":
                freq_lose = 2
                freq_draw = 6
                freq_win = 6
            elif user_mode == "E":
                freq_lose = 5
                freq_draw = 2
                freq_win = 2
            elif user_mode == "C":
                user_is_sure = ""
                while not user_is_sure == "Y":
                    freq_lose = input("freq_lose: ")
                    while inputHandlers.check_for_bad_input_int(freq_lose, [], float("inf")):
                        freq_lose = input("freq_lose: ")
                    freq_lose = int(freq_lose)
                    freq_draw = input("freq_draw: ")
                    while inputHandlers.check_for_bad_input_int(freq_draw, [], float("inf")):
                        freq_draw = input("freq_draw: ")
                    freq_draw = int(freq_draw)
                    freq_win = input("freq_win: ")
                    while inputHandlers.check_for_bad_input_int(freq_win, [], float("inf")):
                        freq_win = input("freq_win: ")
                    freq_win = int(freq_win)
                    logger.info("are you sure you want to play with these chances?")
                    while True:
                        user_is_sure = input()
                        while inputHandlers.check_for_bad_input_strings(user_is_sure):
                            user_is_sure = input()
                        user_is_sure = user_is_sure[0].upper()
                        if user_is_sure == "Y" or user_is_sure == "N":
                            break
                        logger.info("Please put in either [Y]es or [N]o")

            self.list_ai_move_types = (["lose"] * freq_lose) + (["draw"] * freq_draw) + (["win"] * freq_win)

        while True:
            # checks if the game has ended and who won -----------------------------------------------------------------
            self.end_state_of_game = check_state_of_game(self.dic_board)
            if self.end_state_of_game != "":
                break
            # swaps which player has the turn --------------------------------------------------------------------------
            if self.player_who_has_turn == "player 1":
                self.player_who_has_turn = "player 2"
            else:
                self.player_who_has_turn = "player 1"
            # tells the user who is playing this turn and prints board -------------------------------------------------
            logger.info("it is " + self.player_who_has_turn + "'s turn")
            logger.info(print_board(self.dic_board))
            if human_or_ai == "A" and self.player_who_has_turn == "player 2":
                ai_move_type = self.list_ai_move_types[random.randint(0, len(self.list_ai_move_types) - 1)]
                picked_slot = best_move_for_ai(self.dic_board, self.player_who_has_turn, ai_move_type) + 1
            else:
                picked_slot = input("pick a slot\n> ")
            while inputHandlers.check_for_bad_input_int(str(picked_slot), self.list_picked_slots, 10):
                picked_slot = input()
            self.list_picked_slots.append(int(picked_slot))
            # replaces the spot on the board with the player's mark ----------------------------------------------------
            if self.player_who_has_turn == "player 1":
                self.dic_board[list_of_slots[int(picked_slot) - 1]] = "x"
            else:
                self.dic_board[list_of_slots[int(picked_slot) - 1]] = "o"

        # prints the board and who won/lost/drew
        logger.info(print_board(self.dic_board))
        if self.end_state_of_game == "player 1":
            logger.info("player 1 won")
        elif self.end_state_of_game == "player 2" and human_or_ai == "A":
            logger.info("AI won")
        elif self.end_state_of_game == "player 2" and human_or_ai == "H":
            logger.info("player 2 won")
        elif self.end_state_of_game == "ai":
            logger.info("lost")
        else:
            logger.info("Draw")


def game() -> None:
    """
    thing
    :return:
    """
    logger.info("the tic tac toe game has been picked")
    tic_tac_toe = TicTacToe()
    tic_tac_toe.tictactoe_game()


if __name__ == '__main__':
    game()
