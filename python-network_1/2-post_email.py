#!/usr/bin/python3
"""
this module takes a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # get arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # prepare the Data
    # We create a dictionary of our data
    values = {'email': email}

    # it  encodes the data into a query string (format: key=value)
    # and then encode that string into bytes (ascii)
    data = urllib.parse.urlencode(values).encode('ascii')

    # creates the Request object
    # By passing the 'data' argument, urllib automatically uses the POST method
    req = urllib.request.Request(url, data)

    # send the Request and Read Response
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
