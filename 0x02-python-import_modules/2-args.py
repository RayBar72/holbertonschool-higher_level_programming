#!/usr/bin/python3
import sys


def main():
    largo = len(sys.argv)
    if largo == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(largo))
        for i in range(1, largo):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
