class Calc:
    def __init__(self, base_size):
        self.base_size = base_size

    def calc_loop(self):
        rem_target = ""
        while(rem_target != 'n'):
            rem_target = self.get_px()
            self.print_calc(self.calculate(rem_target))

    def calculate(self, px):
        rem = (float(px) / float(self.base_size))

        return rem

    @staticmethod
    def print_calc(rem):
        print(f'{rem}rem')

    @staticmethod
    def get_px():
        px = input('Enter target pixel:\n')

        return px
