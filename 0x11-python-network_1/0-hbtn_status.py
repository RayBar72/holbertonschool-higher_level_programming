#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
import urllib.request


def main():
    """Fuction that gives status of body response of
    holberton intranet
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(html), html, html.decode('utf-8')))


if __name__ == "__name__":
    main()
