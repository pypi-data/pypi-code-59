# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import sys
from getarticle import GetArticle
from os.path import expanduser
import sys

def parse_args():
    parser = ArgumentParser(description='getarticle CLI')
    parser.add_argument('-i', '--input', required=False, \
        help='article DOI or website')
    parser.add_argument('-o', '--output', required=False, \
        help='download direction')
    parser.add_argument('-sd', '--setdownload', required=False, \
        help='set default download direction')
    args = parser.parse_args()
    return args


def main(args):
    if args.setdownload:
        open("%s/.getarticle.ini" %expanduser("~"), "wb").\
            write(args.setdownload.encode())
        return
    ga = GetArticle()
    if not args.input:
        if sys.platform == 'darwin':
            import appscript
            args.input = appscript.app("Safari").windows.first.\
                current_tab.URL()
        else:
            raise ValueError("input is required!")
    ga.input_article(args.input)
    ga.download(direction=args.output)


def entry_point():
    args = parse_args()
    main(args)


if __name__ == '__main__':
    entry_point()
