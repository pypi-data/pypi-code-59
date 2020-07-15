import random


def print_random_hexadecimal_digits(digits: int) -> None:
    # (1) Get the random number
    random_number: int = random.randrange(2 ** (digits * 4))

    # (2) Build a format specifier for the requested number of digits
    format_specifier: str = f"%0{digits}x"

    # (3) Output formatted random number
    print(format_specifier % random_number)
