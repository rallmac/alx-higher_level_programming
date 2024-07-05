#!/bin/bash
# This script takes in a url as input and returns the size of the body
curl -s "$1" | wc -c
