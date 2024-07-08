#!/usr/bin/python3
"""
This script fetches a URL with requests package and returns the body
of the response
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    m = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(m), m))
