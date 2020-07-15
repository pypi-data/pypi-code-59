import math
import matplotlib.pyplot as plt
from .Operation import Operation

class Arithematic(Operation):
    
    def __init__(self, x=10, y=5):
        Operation.__init__(self, x, y)
        
    def add_num(self):
        self.ans = self.x + self.y
        return self.ans

