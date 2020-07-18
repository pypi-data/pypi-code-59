import requests
import websockets
import asyncio
import json
import os
import string
import random
import math

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class Actions:

    @staticmethod
    def move(initial_position, next_positions):

        return {
            "initial_position": initial_position,
            "next_positions": next_positions
        }


class Checkers:
    board_size = 8

    player_down = 'DOWN'
    player_up = 'UP'

    king_type = 1

    def __get_player_str(cell):
        if cell == None:
            return ''
        return cell.get('player')

    def __get_moves_for(board, i, j, to_up = False):
        possible_moves = []

        height = 1
        if to_up:
            height = -1

        x = i-1
        y = j+height
        if x >= 0 and y >= 0 and y < Checkers.board_size and board[x][y] == None:
            possible_moves.append([(i, j), [(x, y)]])

        x = i+1
        y = j+height
        if x < Checkers.board_size and y >= 0 and y < Checkers.board_size and board[x][y] == None:
            possible_moves.append([(i, j), [(x, y)]])

        mx = i-1
        my = j+height
        x = mx-1
        y = my+height
        if x >= 0 and y >= 0 and y < Checkers.board_size and Checkers.__get_player_str(board[mx][my]) == Checkers.player_up and board[x][y] == None:
            possible_moves.append([(i, j), [(x, y)]])

        mx = i+1
        my = j+height
        x = mx+1
        y = my+height
        if x < Checkers.board_size and y >= 0 and y < Checkers.board_size and Checkers.__get_player_str(board[mx][my]) == Checkers.player_up and board[x][y] == None:
            possible_moves.append([(i, j), [(x, y)]])

        return possible_moves

    def __get_possible_moves(board):
        possible_moves = []

        for i in range(Checkers.board_size):
            col = board[i]

            for j in range(Checkers.board_size):
                cell = board[i][j]

                if Checkers.__get_player_str(cell) == Checkers.player_down:
                    possible_moves = possible_moves + Checkers.__get_moves_for(board, i, j)

                    if cell.get('type') == Checkers.king_type:
                        possible_moves = possible_moves + Checkers.__get_moves_for(board, i, j, True)

        return possible_moves

    def flip_the_board(board):
        board = list(zip(*board[::-1]))
        board = list(zip(*board[::-1]))

        for i in range(Checkers.board_size):
            for j in range(Checkers.board_size):
                player = Checkers.__get_player_str(board[i][j])
                if player == Checkers.player_up:
                    board[i][j]['player'] = Checkers.player_down
                elif player == Checkers.player_down:
                    board[i][j]['player'] = Checkers.player_up


        return board

    def flip_the_position(position):
        return (Checkers.board_size-1-position[0], Checkers.board_size-1-position[1])

    def __flip_the_move(move):
        from_position, to_positions = move
        return [Checkers.flip_the_position(from_position), list(map(Checkers.flip_the_position, to_positions))]

    def __flip_the_moves(moves):
        return list(map(Checkers.__flip_the_move ,moves))

    def __is_eating_move(move):
        return math.fabs(move[1][0][1] - move[0][1]) > 1

    def __has_eating_move(moves):
        for move in moves:
            if Checkers.__is_eating_move(move):
                return True

        return False

    def __filter_moves_if_eating(moves):
        if Checkers.__has_eating_move(moves):
            return list(filter(Checkers.__is_eating_move, moves))
        return moves

    def get_possible_moves_for_player(player, board):
        # if player up --> flip the board with colours
        if player == Checkers.player_up:
            board = Checkers.flip_the_board(board)

        moves = Checkers.__get_possible_moves(board)
        print(moves)

        # when returning, if player up --> flip the moves
        if player == Checkers.player_up:
            moves = Checkers.__flip_the_moves(moves)

        # return sorted(moves, key=lambda move: -math.fabs(move[1][0][1] - move[0][1]))
        return Checkers.__filter_moves_if_eating(moves)

    def __init__(self, api_key, strategy):
        self.api_url = os.environ.get("AISPORTS_BACKEND", "http://aisports.ai:3000")
        self.ws_url = os.environ.get("AISPORTS_BACKEND_PLAYER_SOCKET", "ws://aisports.ai:3000")

        self.game_id = None
        self.data = None

        if (not api_key):
            result = requests.post(self.api_url + "/bots", json={
                "data": {
                    "attributes": {
                        "nickname": "python-generated-" + randomString()
                    }
                }
            })
            api_key = result.json().get("data").get("attributes").get("api-key")

        self.api_headers = {
            "X-Api-Key": api_key
        }
        self.strategy = strategy

    async def _listen(self):
        async with websockets.connect(self.ws_url) as websocket:
            await websocket.send(json.dumps({"event": "authenticate", "data": {"key": self.api_headers.get("X-Api-Key")}}))
            stop_socket = False

            while (not stop_socket):
                response = json.loads(await websocket.recv())
                print("[WEBSOCKET] " + str(response))
                event = response.get("event")

                if (event == "game_finished"):
                    print("Game finished, thank you")
                    stop_socket = True
                elif event == "new_game":
                    print("You found new game!")
                    self.game_id = response.get("data").get("gameId")
                    self.data = response.get("data")
                elif event == "turn":
                    self.data = response.get("data")
                    self.__on_turn()

    def __on_turn(self):
        print("Your move")
        action = self.strategy(self.data)
        print("You decided to", action)

        data = {
            "gameId": self.game_id,
            "from": {
                "x": action.get("initial_position")[0],
                "y": action.get("initial_position")[1]
            },
            "to": list(map(lambda position: {"x": position[0], "y": position[1]}, action.get("next_positions")))
        }

        result = requests.post(self.api_url + "/checkers/turn", json=data,
                               headers=self.api_headers)

        if (result.status_code != 200):
            print("[API ERROR]: " + str(result.content))
            result.raise_for_status()

    def start(self):
        print("Searching for opponent ...")
        asyncio.get_event_loop().run_until_complete(self._listen())
