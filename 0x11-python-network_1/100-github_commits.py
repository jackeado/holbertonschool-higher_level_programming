#!/usr/bin/python3
""" Github code challenge"""

from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com'
    uri = '{0}/repos/{1}/{2}/commits'.format(url, argv[2], argv[1])
    req = requests.get(uri).json()

    for com in req[0:10]:
        print(com['sha'] + ':', com['commit']['author']['name'])
