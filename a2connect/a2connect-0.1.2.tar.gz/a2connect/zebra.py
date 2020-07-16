import argparse
import os.path
import yaml

def load_config(fname):
    return yaml.safe_load(fname)

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', dest= 'config', action = 'store', type = str,
        help = 'path to custom config',
        default = os.path.join(os.path.dirname(__file__), "config.yaml")
        )
    return parser

def main():
    parser = build_parser()
    params, other_params = parser.parse_known_args()
    conf = load_config(params.config)
    print("!!!!!! Hello World !!!!!!!")

if __name__ == "__main__":
    main()
