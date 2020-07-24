import shutil
import argparse
import os

def rm_all(filename):
    if os.path.isdir(filename):
        shutil.rmtree(filename)
    elif os.path.isfile(filename):
        os.remove(filename)
    else:
        print("No such file or directory exists")

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("file_or_directory",help="directory or file to be deleted")
    args=parser.parse_args()
    rm_all(args.file_or_directory)
