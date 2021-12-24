#include <stdio.h>
#include <stdlib.h>

/**
*Fibonacci using tail recursion instead of trivial recursion
* fib: fn to find fib of n
*@n: positive int
*return: int: fib of n
*go: helper fuction; eliminates the need to have trivial recursion
*@n: positive int
*@a: current fib number
*@b: next fib number
*/

int fib (int n);
int go (int n, int a, int b);

int main (int argc, char *argv[]){
    int len = 0, i = 0;

    if (argc != 2) {
        printf("Usage: `./1-tail_recursion N` where N is a positive integer\n");
        return 1;
    } else {
        return fib(atoi(argv[1]));
    }
}

int fib (int n){
    return go(n, 0, 1);
}

int go (int n, int a, int b){
    return n == 0 ? a:(n == 1 ? b:go(n - 1, b, a + b));
}