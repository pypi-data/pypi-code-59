# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:14:22 2020

@author: Fatemeh
"""

# __main__.py

import sys
from .parsers import fsl_parser

def main():

    if len(sys.argv) > 1:
        (X, y) = fsl_parser(sys.argv[1])
#    else:
    return (X, y)

if __name__ == "__main__":
    main()