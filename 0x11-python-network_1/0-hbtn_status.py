#!/usr/bin/python3

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

req = request.Request(url)

if __name__ == "__main__":
    with request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t - type:", type(html))
        print("\t - content:", html)
        print("\t - utf8 content:", html.decode('UTF-8'))
