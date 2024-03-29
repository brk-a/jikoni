#!/usr/bin/env python3

'''
Implement tail recursion instead of trivial recursion
Case in point: factorial of n
'''

import sys



def go(n, a):
    ''' Helper function'''
    return a if (n == 1) else go(n - 1, a * n)


def fact(n):
    ''' factorial function'''
    # return go (n, 1)
    print(go(n, 1))


if __name__ == '__main__':
    li = sys.argv
    if len(li) != 2:
        print(f'Usage: `./tail-recursion N` where N is a positive integer\n')
        sys.exit(1)
    else:
        fact(int(li[1]))





