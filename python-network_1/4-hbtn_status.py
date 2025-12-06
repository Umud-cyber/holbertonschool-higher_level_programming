#!/usr/bin/python3
"""
this module fetches https://intranet.hbtn.io/status using the requests package.
it demonstrates how the requests library simplifies HTTP interactions.
"""
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    # the request
    # requests.get() handles the connection and reading in one step.
    response = requests.get(url)

    # accessing the content
    # .text automatically decodes the content based on the headers.
    content = response.text

    # display the details
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
