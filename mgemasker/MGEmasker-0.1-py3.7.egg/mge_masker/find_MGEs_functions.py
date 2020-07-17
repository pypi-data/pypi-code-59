from Bio import SeqIO
import inspect
import sys
import os
import re

def get_mge_patterns(mge_file_path):
    # read text file with pattern match regular expressions and return a list of compiled regexs
    if not mge_file_path:
        mge_file_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], "mge_patterns.txt")))
    mge_patterns = []
    with open(mge_file_path) as mge_file:
        for line in mge_file.readlines():
            pattern = re.compile(r'{line.rstrip()}')
            mge_patterns.append(pattern)
    return(mge_patterns)

def get_features(genome_file_path, file_format):
    record = SeqIO.read(genome_file_path, file_format)
    return(record.features)

def create_gff_line(id, type, start, end, strand, product):
    return(f'{id}\t.\t{type}\t{start}\t{end}\t.\t{strand}\t.\tproduct={product}\n')

def find_mges(features, mge_patterns):
    mges = []
    for feature in features:
        products = feature.qualifiers.get("product")
        if products:
            for product in products:
                for pattern in mge_patterns:
                    if pattern.match(product):
                        if feature.strand:
                            if feature.strand == 1:
                                strand = "+"
                            elif feature.strand == -1:
                                strand = "-"
                        else:
                            strand = "."
                        mges.append(
                            {
                                "type": feature.type,
                                "start": feature.location.start,
                                "end": feature.location.end,
                                "stand": strand,
                                "product": product
                            }
                        )

