#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    post_data = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=argv[1], data=post_data) as response:
        print(response.read().decode('UTF-8'))
