#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    count = 0
    if (x > 0):
        for i in range(x):
            try:
                print("{:d}".format(my_list[idx]), end='')
                idx += 1
                count += 1
            except:
                break
    print('')
    return (count)
