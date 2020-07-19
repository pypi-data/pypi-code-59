import os
import argparse


def _get_files(directory, ignore):
    contents = [os.path.join(directory, o) for o in os.listdir(directory)]
    for _ignore in ignore:
        contents = [o for o in contents if _ignore not in o]
    files = [o for o in contents if os.path.isfile(o)]
    directories = [o for o in contents if os.path.isdir(o)]
    for child_directory in directories:
        files.extend(_get_files(child_directory, ignore))
    return files


def get_files(directories, ignore):
    files = set()
    for directory in directories:
        files = sum(files, set(_get_files(directory, ignore)))
    return files


def get_last_modified(files):
    return set([(o, os.path.getmtime(o)) for o in files])


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directories', nargs='+', default=['.'])
    parser.add_argument('-i', '--ignore', nargs='+', default=[])
    args = parser.parse_args()

    directories = [os.path.abspath(o) for o in args.directories]
    files = get_files(directories, args.ignore)
    print(get_last_modified(files))


if __name__ == '__main__':
    cli()
