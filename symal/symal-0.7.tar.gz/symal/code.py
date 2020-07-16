
import subprocess as sp

from svglib.svglib import svg2rlg

class Test():

    def __init__(self):

        a = sp.run('RNAfold', shell=True, capture_output=True)

        if a.stderr:

            print('Could not run RNAfold')

        else:

            print('Ran sucessfully')

