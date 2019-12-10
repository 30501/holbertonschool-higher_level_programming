#!/usr/bin/python3
# -*- coding: utf-8 -*-
import dis
def magic_calculation(a, b):
    return 98 + (a ** b)
dis.dis(magic_calculation)
