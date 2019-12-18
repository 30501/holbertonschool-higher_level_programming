#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for i in new_string:
        if (i == 'c' or i == 'C'):
            new_string.remove(i)
            return ("".join(new_string))
