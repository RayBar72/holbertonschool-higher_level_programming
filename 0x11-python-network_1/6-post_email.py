#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally
displays the body of the response.
"""
from sys import argv
import requests


def main():
    """Main function that sends an email"""
    varios = {'email': argv[2]}
    r = requests.post(argv[1], varios)
    print("{}".format(r.text))


if __name__ == "__main__":
    main()
