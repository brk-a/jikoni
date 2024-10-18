package main

import (
    "fmt"
    "os"
    "strconv"
)

/**
*Fibonacci using tail recursion instead of trivial recursion
* fib: fn to find fib of n
*@n: positive float
*return: float: fib of n
*goNuts: helper fuction; eliminates the need to have trivial recursion
*@n: positive float
*@a: current fib number
*@b: next fib number
*/

func goNuts(n float64, a float64, b float64) float64 {
	if(n == 0){
		return a;
	} else if(n==1) {
		return b;
	} else {
		return goNuts(n - 1, b, a + b);
	}
}

func fib(n float64) float64 {
	return goNuts(n, 0, 1);
}

func main() {
	if argLength := len(os.Args[1:]); argLength != 2 {
		fmt.Sprintf("Usage: `./1-tail_recursion.go N` where N is a positive integer\n");
		return
	}

	n, err := strconv.ParseFloat(os.Args[1], 64);
	if err!=nil || n < 0 {
        fmt.Printf("Error: %s is not a positive integer\n", os.Args[1]);
        return
    }
    print(fib(n));
}