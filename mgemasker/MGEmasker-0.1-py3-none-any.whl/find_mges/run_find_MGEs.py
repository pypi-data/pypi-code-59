#!/usr/bin/env python3
import argparse
import sys
from find_mges.find_MGEs_functions import get_mge_patterns

class EnhancedParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def parse_args():
    parser = EnhancedParser()
    parser.add_argument('-i', '--genome_file_path', help='path to a genome file', required=True)
    parser.add_argument('-f', '--file_format', help='genome file format', default = "genbank")
    parser.add_argument('-m', '--mge_file_path', help='path to a file containing regex MGE annotations')
    return(parser.parse_args())


def main():
    options = parse_args()
    mge_patterns = get_mge_patterns(options.mge_file)
 

if __name__ == "__main__":
    main()

