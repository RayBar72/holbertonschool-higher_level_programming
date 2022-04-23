#!/usr/bin/python3
"""Script that takes an URL an sends an email"""
from sys import argv
from urllib import request, parse


def main():
    """Main fucntion that sends an email"""
    values = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], values) as r:
        print("{}".format(r.read().decode('utf-8')))


if __name__ == "__main__":
    main()
