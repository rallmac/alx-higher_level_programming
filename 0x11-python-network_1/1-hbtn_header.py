#!/usr/bin/python3
"""This script takes in a url and an email the passed url"""

import urllib.request
import sys


if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.getheaders()

    x_request_id = dict(headers).get('X-Request-Id')

print(x_request_id)
