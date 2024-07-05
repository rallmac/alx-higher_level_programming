#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and the server respondes with the message 'You got me!'
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
