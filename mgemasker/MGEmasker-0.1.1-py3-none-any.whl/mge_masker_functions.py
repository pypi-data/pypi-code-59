from Bio import SeqIO
import inspect
import sys
import os
import re
from pathlib import Path

def get_mge_patterns(mge_file_path = None):
  # read text file with pattern match regular expressions and return a list of compiled regexs
  if not mge_file_path:
    mge_file_path = os.path.join(os.path.dirname(__file__), "mge_patterns.txt")
  mge_patterns = []
  with open(mge_file_path) as mge_file:
    for line in mge_file.readlines():
      pattern = re.compile(line.rstrip())
      mge_patterns.append(pattern)
  return(mge_patterns)

def get_features(genome_file_path, file_format):
  record = SeqIO.read(genome_file_path, file_format)
  return(record.features)

def create_gff_line(accession, mge):
  return(f'{accession}\t.\t{mge["type"]}\t{mge["start"]}\t{mge["end"]}\t.\t{mge["strand"]}\t.\tproduct="{mge["product"]}"\n')

def search_features_for_patterns(features, mge_patterns):
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
                "start": feature.location.start.position + 1,
                "end": feature.location.end.position,
                "strand": strand,
                "product": product
              }
            )
  return(mges)

def find_mges(genome_file_path, file_format, mge_file_path = None):
  features = get_features(genome_file_path, file_format)
  mge_patterns = get_mge_patterns(mge_file_path)
  mges = search_features_for_patterns(features, mge_patterns)
  return(mges)

def create_mge_gff_file(genome_file_path, file_format, mges):
  record = SeqIO.read(genome_file_path, file_format)
  gff_file_path = Path(genome_file_path).with_suffix('.gff')
  with open(gff_file_path, "w") as gff_file:
    for mge in mges:
      gff_file.write(create_gff_line(record.name, mge))
  return(gff_file_path)
  


  