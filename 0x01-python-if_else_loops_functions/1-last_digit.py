#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pnumber = number
if (number < 0):
    pnumber = number * -1
ldigit = pnumber % 10
if (ldigit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, ldigit))
elif (ldigit < 6 and ldigit != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, ldigit))
else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, ldigit))
