#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL
# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request to the provided URL and display the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
