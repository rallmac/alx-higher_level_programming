#!/bin/bash
# This bash script takes in a url as an argument sends a get request and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
