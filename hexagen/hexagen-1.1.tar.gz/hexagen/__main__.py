import random
import argparse


def main(digits: int) -> None:
    # (1) Get the random number
    random_number: int = random.randrange(2 ** (digits * 4))

    # (2) Build a format specifier for the requested number of digits
    format_specifier: str = f"%0{digits}x"

    # (3) Output formatted random number
    print(format_specifier % random_number)


if __name__ == "__main__":
    # Define command line arguments
    parser = argparse.ArgumentParser(
        prog="hexagen",
        description="Generates random hexadecimal digits and prints them to standard output.",
    )
    parser.add_argument(
        "--digits", type=int, default=6, help="number of random hexadecimal digits"
    )
    args = parser.parse_args()

    main(args.digits)
