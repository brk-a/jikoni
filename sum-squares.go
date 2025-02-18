package sum_squares

import (
	"fmt"
	"os"
	"strconv"
)

func square(num string) (ret int) {
	var result int
	result = strconv.Atoi(num) * strconv.Atoi(num)
	return result
}

func main() {
	sum := 0
	i := len(os.Args)

	if i == 1 {
		return
	} else {

		sum += square(os.Args[i-1]) /* cannot call because square expects int, not strconv.Atoi(os.Args[i-1]) */
	}
	fmt.Printf("%d", sum)
}
