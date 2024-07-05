#!/usr/bin/python3

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

    Raises:
    urllib.error.HTTPError: If an HTTP error occurs.
    urllib.error.URLError: If a URL error occurs.
    Exception: If any other error occurs.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
    except urllib.error.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except urllib.error.URLError as url_err:
        print(f"URL error occurred: {url_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
