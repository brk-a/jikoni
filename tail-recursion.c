#include <stdio.h>

/**
*Calculate the factorial of a number using tail recursion instead of trivial recursion
* fact: fn to calc factorial of n
*@n: positive int
*return: int: factorial of n
*go: helper fuction; eliminates the need to have trivial recursion
*@n: positive int
*@a: cumulative product
*/

int fact (int n);
int go (int n, int a);

int main (int __attribute__ ((unused)) argc, int argv){
    int len = 0;
    while (argv) {
        len++;
    }
    
    if (len != 2) {
        printf('Usage: `./0-tail_recursion N` where N is a positive integer\n');
        return 1;
    } else {
        return fact(argv[1]);
    }
}

fact(n){
    return go(n, 1);
}

go(n, a){
    return n == 1 ? a : go(n - 1, a * n);
}