#!/usr/bin/python3
"""
this module takes a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    # get the URL from command line arguments
    url = sys.argv[1]

    # send the Request
    with urllib.request.urlopen(url) as response:
        # access the Headers
        # the response object has a .headers attribute (or .info())
        # that acts like a dictionary.

        # it uses .get() to safely retrieve 'X-Request-Id'.
        # if it doesn't exist, it returns None (and prints 'None' or nothing).
        print(response.headers.get('X-Request-Id'))
