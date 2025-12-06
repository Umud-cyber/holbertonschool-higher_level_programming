#!/usr/bin/python3
"""
this module fetches https://intranet.hbtn.io/status using the urllib package.
it demonstrates how to make a simple GET request and display response details.
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    # request
    # it uses 'with' to ensure the connection is closed automatically
    with urllib.request.urlopen(url) as response:
        # read the body
        body = response.read()

        # display the details
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8'))
