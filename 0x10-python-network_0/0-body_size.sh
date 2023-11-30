#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL
# Checks if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
