#!/usr/bin/python3
def raise_exception():
    try:
        num = 5
        num.append(10)
    except TypeError:
        raise
