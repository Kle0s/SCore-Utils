#! /usr/bin/python3
import sys
import re


def grep_file(f, token):
    text = ""
    with open(f, "r") as fl:
        for line in fl.read().split("\n"):
            for word in line.split(" "):
                if word == token:
                    text += line
                    text += "\n"
    return text

def grep_stdin(token):
    for line in sys.stdin.read().split("\n"):
        if token in line.split(" "):
            sys.stdout.write(line + "\n")


if __name__ == '__main__':

    if len(sys.argv) == 2:
        grep_stdin(sys.argv[1])
    elif len(sys.argv) >= 3:
        if "--help" in sys.argv:
            sys.stdout.write("No help yet, Im too la<y\n")
            sys.argv.remove("--help")
            sys.exit()

        for arg in sys.argv[2:]:
            sys.stdout.write(grep_file(arg, sys.argv[1]))

    else:
        sys.stderr.write("Too few arguments!\n")
        sys.stderr.write("Usage: sgrep.py token file(s)\n")
        sys.exit()

