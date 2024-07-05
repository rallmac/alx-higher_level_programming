#!/bin/bash
# Write a bash script that sends a json post request to a url and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
