import click
from rem_calc.rem import Calc


@click.group()
def main():
    pass


@click.command()
@click.option('--base', prompt='Enter base pixel', help='REM Pixel Base')
def interactive(base):
    calc = Calc(base)
    calc.calc_loop()


@click.command()
@click.option('--base', prompt='Enter base pixel', help='REM Pixel Base')
@click.option('--target', prompt='Enter target pixel', help='REM Pixel Target')
def calculate(base, target):
    calc = Calc(base)
    calc.print_calc(calc.calculate(target))


main.add_command(interactive)
main.add_command(calculate)

if __name__ == "__main__":
    main()
