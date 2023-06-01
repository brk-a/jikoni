'''
Implement tail recursion instead of trivial recursion
Case in point: nth Fibonacci number
'''

import sys


def go(n, a, b):
    ''' Helper function'''
    return a if (n == 0) else b if n == 1 else go(n - 1, b, a + b)


def fib(n):
    ''' fib function'''
    return go (n, 0, 1)


if __name__ == '__main__':
    li = sys.argv
    if len(li) != 2:
        print(f'Usage: `./1-tail_recursion N` where N is a positive integer\n')
        sys.exit(1)
    else:
        fact(li[1])





