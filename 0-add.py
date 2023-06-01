#!/usr/bin/python3

import os
import sys

def add(a, b):
    return a + b

if __name__=='__main__':
    if len(sys.argv) != 3:
        print('usage ...')
        sys.exit(0)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f'{a} + {b} = {add(a, b)}')
    sys.exit(0)