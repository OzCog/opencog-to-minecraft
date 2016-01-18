import os
import sys
import argparse

arg_parser = argparse.ArgumentParser(description="Align coding style \
            according to PEP8 guidelines.")

arg_parser.add_argument("-c", "--check", action="store_true")
arg_parser.add_argument("-p", "--preview", action="store_true")
arg_parser.add_argument("-r", "--refactor", action="store_true")

arg_parser.add_argument("-a", "--all", action="store_true")
arg_parser.add_argument("-i", "--interactive", action="store_true")

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


def refactor_autopep8_all():
    directory = "minecraft_bot/src/"
    all_filenames = [f for f in os.listdir(directory)
                 if os.path.isfile(os.path.join(directory, f))]

    for filename in all_filenames:
        if filename[-3:] == ".py":
            refactor_autopep8(directory + filename)


def start_interactive_mode():
    print "***** INTERACTIVE MODE *****"
    arg_parser.print_help()
    new_task = "y"

    while new_task == "y":
        filename = "minecraft_bot/src/" + raw_input("Enter filename: ")
        action = raw_input("Choose action [c/p/r]: ")
        if action == "c":
            check_pep8_errors(filename)
        elif action == "p":
            preview_autopep8(filename)
        elif action == "r":
            refactor_autopep8(filename)
        else:
            print "Not a valid option! "

        new_task = raw_input("Proceed with new task? [y/n]: ")


if __name__ == '__main__':
    arguments = vars(arg_parser.parse_args(sys.argv[1:]))

    if arguments["all"]:
        refactor_autopep8_all()
    elif arguments["interactive"]:
        start_interactive_mode()
    else:
        python_filename = "minecraft_bot/src/" + arguments["file"]

        if arguments["check"]:
            check_pep8_errors(python_filename)

        if arguments["preview"]:
            preview_autopep8(python_filename)

        if arguments["refactor"]:
            refactor_autopep8(python_filename)
