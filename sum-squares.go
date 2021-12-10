package main

import (
	"fmt"
	"os"
	"strconv"
)

func square(num int) (ret int) {
	return num * num
}

func main() {
	sum := 0
	i := len(os.Args)

	if i == 1 {
		return
	} else {

		sum += square(strconv.Atoi(os.Args[i-1]))
	}
	fmt.Printf("%d", sum)
}
