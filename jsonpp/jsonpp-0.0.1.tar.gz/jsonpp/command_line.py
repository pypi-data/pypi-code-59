import jsonpp
import sys


def main():
    data = sys.stdin.read()
    jsonpp.pretty_print(data)


if __name__ == "__main__":
    main()
