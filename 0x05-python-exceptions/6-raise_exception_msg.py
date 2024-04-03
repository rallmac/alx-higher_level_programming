#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise UndefinedNameError(message)
    except NameError:
        raise
