'''
CLI for the BallBoi Package
'''

#------------------------------------------------------------------------------
# Standard Library From Imports
#------------------------------------------------------------------------------
from argparse import ArgumentParser

#------------------------------------------------------------------------------
# Non-Standard Library From Imports
#------------------------------------------------------------------------------
from strotools.ballboi.nfl_retriever import add_nfl_parser_to_subparser

def parse_args(parser=None,
               parserName: str = ''):
    '''
    Parse args for this CLI.

    Args:
      [Optional] parser::ArgumentParser
        If no parser is passed in, a new parser is created
      [Optional] parserName::str
        Name to give parser if new one created within this function
    '''
    if not parser:
        parser = ArgumentParser(parserName)

    subparser = parser.add_subparsers(help='BallBoi commands')
    add_nfl_parser_to_subparser(subparser)

    return parser.parse_args()
    

def main():
    args = parse_args()