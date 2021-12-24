#!/usr/bin/python3

'''
Make pseudo-random numbers using Linear Feedback Shift Register (LFSR)
'''

import sys

def lfsr(num):
    '''LFSR function'''
    
    num = num if num and isinstance(num, int) else None

    if len(sys.argv) != 2 or not num:
        print(f'Usage: `./0-lfsr.py N` where N is a positive integer')
        sys.exit(1)

    state = (1 << num) | 1

    while True:
        print(f'{state & 1}', end='')
        newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
        state = (state >> 1) | (newbit << num)

    print(f'The "random number" is {state}')
    return state

if __name__ == '__main__':
    lfsr(127)