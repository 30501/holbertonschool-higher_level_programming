#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    a = args[0]
    b = args[1]
    try:
        result = fct(a, b)
    except Exception as e:
        s = "Exception: " + str(e) + "\n"
        sys.stderr.write(s)
        return (None)
    return (result)
