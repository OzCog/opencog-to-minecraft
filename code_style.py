import os
import sys
import argparse

arg_parser = argparse.ArgumentParser(description="Align coding style \
            according to PEP8 guidelines.")

arg_parser.add_argument("-c", "--check", action="store_true")
arg_parser.add_argument("-p", "--preview", action="store_true")
arg_parser.add_argument("-r", "--refactor", action="store_true")
arg_parser.add_argument("-f", "--file")


def check_pep8_errors(filename):
    print "***** PEP8 errors in " + filename.split("/")[2] + " *****"
    os.system("pep8 " + filename)
    print "DONE !\n\n"


def preview_autopep8(filename):
    print "***** After refactoring " + filename.split("/")[2] + " *****"
    os.system("autopep8 " + filename)
    print "DONE !\n\n"


def refactor_autopep8(filename):
    print "***** Refactoring " + filename.split("/")[2] + " *****"
    os.system("autopep8 -i -a " + filename)
    print "DONE !\n\n"


if __name__ == '__main__':
    arguments = vars(arg_parser.parse_args(sys.argv[1:]))
    python_filename = "minecraft_bot/src/" + arguments["file"]

    if arguments["check"]:
        check_pep8_errors(python_filename)

    if arguments["preview"]:
        preview_autopep8(python_filename)

    if arguments["refactor"]:
        refactor_autopep8(python_filename)

