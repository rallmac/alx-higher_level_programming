#!/bin/bash
# This bash script takes in a url and sends a post request and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
