class Cell:
    '''Class used to represent a cell with a state and it address on a map'''

    def __init__(self, n, status='dead'):
        self.status = status
        self.n = n
        self.address = {'x': 'unset', 'y': 'unset'}

    def __str__(self):
        return 'X' if self.status == 'dead' else 'V'

    def revive(self):
        self.status = 'alive'

    def die(self):
        self.status = 'dead'

    def set_address(self, x, y):
        self.address['x'] = x
        self.address['y'] = y
