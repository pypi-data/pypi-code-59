import requests
import argparse
from pprint import pprint
from libgen import Scraper

def main():
    args = argparse.ArgumentParser(description="cli tool for library genesis")
    args.add_argument("--search", help="search the library")
    args.add_argument("--download", help="download a file")
    args.add_argument("--output", help="output file name")
    res = args.parse_args()


    if res.search:
        search_term = res.search
        data = Scraper.get_data(search_term)
        pprint(data)
    if res.download:
        link = res.download
        if res.output:
            output_path = res.output
        else:
            output_path = None
        output = Scraper.download(link, output_path)
        if not output:
            print('Invalid url')