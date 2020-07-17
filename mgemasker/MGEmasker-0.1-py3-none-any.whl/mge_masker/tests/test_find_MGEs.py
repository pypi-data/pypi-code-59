import pytest
import os
import inspect
import tempfile
from mge_masker.mge_masker_functions import find_mges, create_mge_gff_file

@pytest.fixture(scope="module")
def test_genome_file_path():
  test_genome_file_path = os.path.realpath(
    os.path.abspath(
      os.path.join(
        os.path.split(inspect.getfile( inspect.currentframe() ))[0],
        "data",
        "test.gbk"
      )
    )
  )
  return(test_genome_file_path)

@pytest.fixture(scope="module")
def expected_gff_file_path():
  expected_gff_file_path = os.path.realpath(
    os.path.abspath(
      os.path.join(
        os.path.split(inspect.getfile( inspect.currentframe() ))[0],
        "data",
        "test.gff"
      )
    )
  )
  return(expected_gff_file_path)

@pytest.fixture(scope="module")
def expected_mges():
  return (
    [
      {'type': 'CDS', 'start': 201, 'end': 400, 'strand': '+', 'product': 'Transposon'},
      {'type': 'CDS', 'start': 401, 'end': 500, 'strand': '-', 'product': 'Phage protein'},
      {'type': 'CDS', 'start': 501, 'end': 600, 'strand': '+', 'product': 'IS101'},
      {'type': 'CDS', 'start': 601, 'end': 700, 'strand': '+', 'product': 'Integrase'}
    ]
  )
def test_find_mges(test_genome_file_path, expected_mges):
  mges = find_mges(test_genome_file_path, "genbank")
  
  for index, mge in enumerate(mges):
    assert mge == expected_mges[index]
    
def test_create_file(test_genome_file_path, expected_gff_file_path):
  with tempfile.NamedTemporaryFile(mode = "w") as temp_genome:
    with open(test_genome_file_path) as test_genome_file:
      genome_string = test_genome_file.read()
    temp_genome.write(genome_string)
    temp_genome.flush()
    mges = find_mges(temp_genome.name, "genbank")
    gff_file_path = create_mge_gff_file(temp_genome.name, "genbank", mges)
    with open(gff_file_path) as gff_file:
      gff_string = gff_file.read()
    with open(expected_gff_file_path) as expected_gff_file:
      expected_gff_string = expected_gff_file.read()
    assert gff_string == expected_gff_string
      
