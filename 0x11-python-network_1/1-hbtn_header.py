#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
from urllib import request
from sys import argv


def main():
    """Main funtion that prints X-Request-Id"""
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        o = r.info()
        o = dict(o)
    print("{}".format(o['X-Request-Id']))


if __name__ == "__main__":
    main()
