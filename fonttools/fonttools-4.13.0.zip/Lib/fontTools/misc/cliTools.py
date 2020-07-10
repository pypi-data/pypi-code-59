"""Collection of utilities for command-line interfaces and console scripts."""
from fontTools.misc.py23 import *
import os
import re


numberAddedRE = re.compile(r"#\d+$")


def makeOutputFileName(input, outputDir=None, extension=None, overWrite=False):
    """Generates a suitable file name for writing output.

    Often tools will want to take a file, do some kind of transformation to it,
    and write it out again. This function determines an appropriate name for the
    output file, through one or more of the following steps:

    - changing the output directory
    - replacing the file extension
    - suffixing the filename with a number (``#1``, ``#2``, etc.) to avoid
      overwriting an existing file.

    Args:
        input: Name of input file.
        outputDir: Optionally, a new directory to write the file into.
        extension: Optionally, a replacement for the current file extension.
        overWrite: Overwriting an existing file is permitted if true; if false
            and the proposed filename exists, a new name will be generated by
            adding an appropriate number suffix.

    Returns:
        str: Suitable output filename
    """
    dirName, fileName = os.path.split(input)
    fileName, ext = os.path.splitext(fileName)
    if outputDir:
        dirName = outputDir
    fileName = numberAddedRE.split(fileName)[0]
    if extension is None:
        extension = os.path.splitext(input)[1]
    output = os.path.join(dirName, fileName + extension)
    n = 1
    if not overWrite:
        while os.path.exists(output):
            output = os.path.join(
                dirName, fileName + "#" + repr(n) + extension)
            n += 1
    return output
