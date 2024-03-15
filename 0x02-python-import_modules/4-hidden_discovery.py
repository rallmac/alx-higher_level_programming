#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfsn = dir()
    for i in range(0, len(allfsn)):
        if allfsn[i][:2] != "_":
            print("{:s}".format(allfsn[i]))
