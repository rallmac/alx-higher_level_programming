#!/bin/bash
# This bash script sends a delete request passed to it and displays the body of the response
curl -sX DELETE "$1"
