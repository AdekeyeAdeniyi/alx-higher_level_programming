#!/bin/bash
# Bash script that takes in a URL, print response body if status code = 200
if [ "$(curl -sLw "%{http_code}" "$1" -o /dev/null)" -eq "200" ]; then curl -sL "$1"; fi
