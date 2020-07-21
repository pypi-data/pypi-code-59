from gameoflife.game.Cell import Cell
from gameoflife.game.Form import Form
import random


class Runner:
    '''Class wich provide a map of cells and
     manage their behaviour through rules'''

    to_revive = []
    to_kill = []
    forms = Form

    def __init__(self, forms_amount=50, density=100, size=50, initial_status="dead", rounds=50):
        self.density = density
        self.size = size
        self.map = self.generate_map(initial_status, size)
        self.set_addresses()
        self.generate_forms(forms_amount)
        self.rounds = rounds

    def generate_map(self, initial_status, size):
        return [[Cell((i + 1) * (_ + 1), initial_status) for i in range(size)] for _ in range(size)]

    def generate_forms(self, amount):
        for _ in range(amount):
            tries = 10
            shape = Form.get_shape()
            placable = False
            while placable is not True and tries > 0:
                tries -= 1
                random_point = self.get_random_point()
                placable = self.check_place(random_point, shape)
                if placable:
                    self.place(random_point, shape)

        return

    def check_place(self, origin, shape):
        for x_index in range(Form.get_shape_form(shape)["x"]):
            for y_index in range(Form.get_shape_form(shape)["y"]):
                x = (origin['x'] + x_index) % self.size
                y = (origin['y'] + y_index) % self.size
                if self.is_free(x, y) is not True:
                    return False
        return True

    def place(self, origin, shape):
        for x_index in range(Form.get_shape_form(shape)["x"]):
            for y_index in range(Form.get_shape_form(shape)["y"]):
                x = (origin['x'] + x_index) % self.size
                y = (origin['y'] + y_index) % self.size
                self.map[y][x].status = 'alive' if shape[y_index][x_index] == 'a' else 'dead'

        return

    def is_free(self, x, y):
        x %= self.size
        y %= self.size
        return True if self.map[y][x].status == 'dead' else False

    def get_random_point(self):
        return {
            'x': random.randint(0, self.size - 1),
            'y': random.randint(0, self.size - 1)
        }

    def set_addresses(self):
        for i in range(len(self.map)):
            y = i
            for j in range(len(self.map[i])):
                cell = self.map[i][j]
                x = j
                cell.set_address(x, y)

    def run(self):
        if self.rounds < 0:
            return

        for cell_line in self.map:
            for cell in cell_line:
                self.try_kill(cell) if cell.status == 'alive' else self.try_revive(cell)
        self.update()
        self.reset()
        self.rounds -= 1

    def try_kill(self, cell):
        neighbourhood = self.get_neighborhood(cell)
        if len(neighbourhood) != 2 and len(neighbourhood) != 3:
            self.to_kill.append(cell)

    def try_revive(self, cell):
        neighbourhood = self.get_neighborhood(cell)
        if len(neighbourhood) == 3:
            self.to_revive.append(cell)

    def get_neighborhood(self, cell):
        neigbhors = []
        top_y_index = cell.address['y'] - \
            1 if cell.address['y'] > 0 else self.size - 1
        bot_y_index = cell.address['y'] + \
            1 if cell.address['y'] < self.size - 1 else 0

        for y in [top_y_index, cell.address['y'], bot_y_index]:
            left_x_index = cell.address['x'] - \
                1 if cell.address['x'] > 0 else self.size - 1
            right_x_index = cell.address['x'] + \
                1 if cell.address['x'] < self.size - 1 else 0
            for x in [left_x_index, cell.address['x'], right_x_index]:
                neigbhors.append(self.map[y][x])

        return [n for n in neigbhors if n.status == 'alive' and n is not cell]

    def update(self):
        for cell in self.to_revive:
            cell.revive()

        for cell in self.to_kill:
            cell.die()

    def reset(self):
        self.to_kill = []
        self.to_revive = []

    def __str__(self):
        return ('\ndensity = ' + str(self.density) + '\nsize = ' + str(self.size) + '\npopulation = \n' + self.stringify_map())

    def stringify_map(self):
        full_cells = [[str(cell) for cell in cell_array]
                      for cell_array in self.map]
        for i in range(len(full_cells)):
            print(full_cells[i])

        return str(full_cells)
