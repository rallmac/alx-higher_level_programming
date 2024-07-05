#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def fetch_status(url):
    """
    Fetches the status from the given URL and prints the response details.

    The details printed include:
    - The type of the response body
    - The raw content of the response body
    - The UTF-8 decoded content of the response body

    Args:
    url (str): The URL to fetch the status from.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
