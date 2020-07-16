import plotly.graph_objects as go
from plotly.subplots import make_subplots

from figure import add_molecule


class Subplot():

    __init__(self, nrows, ncolumns):
    self.fig = make_subplots()
    self.nrows = nrows
    self.ncolumns = ncolumns 


    def add_molecule(self, name, molecule, position):
