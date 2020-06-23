#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
"""
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as req:
        print(req.getheader("X-Request-Id"))
