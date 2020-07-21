from tkinter import Tk
from Vallegameoflife.game.Runner import Runner
from Vallegameoflife.screens.GameOfLife import GameOfLife
from Vallegameoflife.screens.Ihm import IHM

input_interface = IHM()

while input_interface.replay:

    input_interface.launch(Tk())
    values = input_interface.values
    if values:
        runner = Runner(size=values[0], rounds=values[1], forms_amount=values[2])
    else:
        print('Running with default parameters ...')
        runner = Runner()

    game_interface = GameOfLife(runner)
    game_interface.launch()

    input_interface.pop_up(Tk())