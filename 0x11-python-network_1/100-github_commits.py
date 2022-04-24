#!/usr/bin/python3
"""
Script that takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
"""
from sys import argv
import requests


def main():
    """Main fuction of challenge"""
    direc = 'https://api.github.com/repos/{}/{}/commits'\
            .format(argv[2], argv[1])
    r = requests.get(direc)
    i = 0
    for x in r.json():
        if i < 10:
            print("{}: {}".format(x.get("sha"),
                  x.get('commit').get('author').get('name')))
        i += 1


if __name__ == "__main__":
    main()
