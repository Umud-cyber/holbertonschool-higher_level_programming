#!/usr/bin/python3
"""
this module sends a request to a URL and displays the body of the response.
it handles HTTP errors (like 404, 500) gracefully.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # get the URL
    url = sys.argv[1]

    try:
        # attempt the request
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))

    except urllib.error.HTTPError as e:
        # catch HTTP Errors (4xx, 5xx)
        # the exception object 'e' contains the status code (e.code)
        print("Error code: {}".format(e.code))
