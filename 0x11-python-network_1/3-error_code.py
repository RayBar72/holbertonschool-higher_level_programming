#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
from urllib import error, request
from sys import argv


def main():
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print("{}".format(r.read().decode('utf-8')))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except error.URLError as e:
        print("Error code: {}".format(e.reason))


if __name__ == '__main__':
    main()
