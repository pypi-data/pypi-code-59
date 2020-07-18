import sys

def printHelp():
    print('EMPTY')
    print('python -m pyuts.py_crawl scrapy_init projectName')

if __name__ == "__main__":
    option = '--help'
    if len(sys.argv) > 1:
        option = sys.argv[1]
    if option in ['-h','--help']:
        printHelp()
        