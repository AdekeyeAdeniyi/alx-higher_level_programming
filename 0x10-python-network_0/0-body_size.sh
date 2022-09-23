#!/bin/bash
#Prints the size of the body of the response
curl -sI "$1" | grep "content-length" | awk '{print $2}'
