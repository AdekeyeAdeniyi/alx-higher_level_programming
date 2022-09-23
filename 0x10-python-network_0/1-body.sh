#!/bin/bash
# Bash script that takes in a URL, print response body if status code = 200
if [ "$(curl -sI "$1"| head -n 1 | cut -d$' ' -f2 )" -eq '200' ]; then curl -s "$1"; fi
