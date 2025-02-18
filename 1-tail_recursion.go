package recursion

import (
    "fmt"
    "os"
    "strconv"
)

/**
*Fibonacci using tail recursion instead of trivial recursion
* fib: fn to find fib of n
*@n: positive int
*return: int: fib of n
*goNuts: helper fuction; eliminates the need to have trivial recursion
*@n: positive int
*@a: current fib number
*@b: next fib number
*/

func goNuts(n int64, a int64, b int64) int64 {
	if(n == 0){
		return a;
	} else if(n==1) {
		return b;
	} else {
		return goNuts(n - 1, b, a + b);
	}
}

func fib(n int64) int64 {
	return goNuts(n, 0, 1);
}

func main() {
	if argLength := len(os.Args[1:]); argLength != 2 {
		fmt.Sprintf("Usage: `./1-tail_recursion.go N` where N is a positive integer\n");
		return
	}

	n, err := strconv.ParseInt(os.Args[1], 0, 64);
	if err!=nil || n < 0 {
        fmt.Printf("Error: %s is not a positive integer\n", os.Args[1]);
        return
    }
    print(fib(n));
}