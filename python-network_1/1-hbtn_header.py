#!/usr/bin/python3
import sys
import urllib.request
url = sys.argv
with urllib.request.urlopen(url) as response
    header = response.getheader('X-Request-Id')
    print("\t- value: {}".format(header))
