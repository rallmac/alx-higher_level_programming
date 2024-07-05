#!/bin/bash
# This script takes in a url as input and returns the
# size of the body

if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

response_size=$(curl -s -w '%{size_download}' -o /dev/null "$URL")

echo "${response_size}"
