#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    opera = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op in opera:
        print("{} {} {} = {}".format(argv[1],
                                     argv[2], argv[3], opera[op](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
