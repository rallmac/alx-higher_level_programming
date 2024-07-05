#!/bin/bash
# This bash script takes in a url and displays all acceptable server methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
