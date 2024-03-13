#!/usr/bin/python3

for mynumber in range(0, 100):
    if mynumber == 99:
        print("{}".format(mynumber))
    else:
        print("{:02d}, ".format(mynumber), end='')
