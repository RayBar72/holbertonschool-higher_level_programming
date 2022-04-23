#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL
and displays the body of the response.
'''
import requests
from sys import argv


def main():
    '''Main function that handles error code'''
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))


if __name__ == "__main__":
    main()
