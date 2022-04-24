#!/usr/bin/python3
"""
Scritp that takes Github credentials an usese Api to display id
"""
from sys import argv
import requests


def main():
    auth = (argv[1], argv[2])
    dir = 'https://api.github.com/user'
    r = requests.get(dir, auth=auth)
    try:
        print("{}".format(r.json().get('id')))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
