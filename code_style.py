import os
import sys
import argparse

arg_parser = argparse.ArgumentParser(description="Align coding style \
            according to PEP8 guidelines.")

arg_parser.add_argument("-c", "--check", action="store_true")
arg_parser.add_argument("-f", "--file")


def check_pep8_errors(f):
    os.system("pep8 " + python_file)


if __name__ == '__main__':
    arguments = vars(arg_parser.parse_args(sys.argv[1:]))
    python_file = "minecraft_bot/src/" + arguments["file"]

    if arguments["check"]:
        check_pep8_errors(python_file)
