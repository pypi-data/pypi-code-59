import ptc

from ptc_cli import parser


def main() -> None:
    p = parser.make()
    args = p.parse_args()

    with open(args.file) as f:
        lines = f.readlines()

    calibration_input = []

    for l in lines:
        numbers = [float(n.strip()) for n in l.split(",")]
        point = tuple(numbers[:3])
        rotation = tuple(numbers[3:])
        calibration_input.append((point, rotation))

    calibration_result = ptc.calibrate(calibration_input)
    print("Calculated TCP offset: {}".format(calibration_result.x))
    if args.verbose:
        print("More detailed calibration info:\n{}".format(calibration_result))
