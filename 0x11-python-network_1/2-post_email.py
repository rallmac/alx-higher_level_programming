#!/usr/bin/python3
"""
Usage: python script.py <URL>
This script fetches the X-Request-Id from the
headers of a response from the given URL.
"""

import urllib.request
import sys

# Check if the script receives the URL as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

# The URL is the first argument
url = sys.argv[1]

try:
    # Use a with statement to send the request and handle the response
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.getheaders()

        # Find the value of the X-Request-Id header
        x_request_id = dict(headers).get('X-Request-Id')

        # Print the value of the X-Request-Id header
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")

except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print(f"Failed to reach the server. Reason: {e.reason}")
    elif hasattr(e, 'code'):
        print(f"Failed to fulfill the request. Error code: {e.code}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
