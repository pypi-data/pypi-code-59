#!/usr/bin/env python3
import argparse
import sys
from mge_masker.mge_masker_functions import get_mge_patterns, find_mges, create_mge_gff_file

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
    mges = find_mges(options.genome_file_path, options.file_format, options.mge_file_path)
    gff_file_path = create_mge_gff_file(options.genome_file_path, options.file_format, mges)
    print(f'GFF file written to {gff_file_path}')
    
 

if __name__ == "__main__":
    main()

