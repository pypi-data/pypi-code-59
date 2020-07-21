import argparse


def make() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        "Calculate robot tool offset", allow_abbrev=False
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Absolute path to file with robot positions",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Provide additional info about the calibration procedure result",
    )
    return parser
