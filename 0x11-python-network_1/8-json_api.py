"""Write a Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
        data = response.json
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except ValueError:
        print("No result")
