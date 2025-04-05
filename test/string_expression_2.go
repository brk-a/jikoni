package main

import (
	"fmt"
	"strings"
)

// StringExpression function to convert written-out expression to a number
func StringExpression(str string) string {
	// Define mappings for numbers and words
	wordsToNumbers := map[string]int{
		"zero":  0, "one": 1, "two": 2, "three": 3, "four": 4,
		"five":  5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
	}

	// Handling the operations as well: "plus" or "minus"
	operations := map[string]string{
		"plus":  "+", "minus": "-",
	}

	// Initialize variables
	var currentNum int
	var lastOperation string
	varFiltersCg := []string{}

	// Split the string into parts for number and operations
	for i := 0; i < len(str); i++ {
		// Attempt to read a number or operation from the string
		for word, number := range wordsToNumbers {
			if strings.HasPrefix(str[i:], word) {
				// If it's a number, add it to currentNum or apply lastOperation
				if lastOperation == "" {
					currentNum = number
				} else {
					if lastOperation == "+" {
						currentNum += number
					} else if lastOperation == "-" {
						currentNum -= number
					}
				}
				// Add the number to the output list for the final result
				varFiltersCg = append(varFiltersCg, word)
				i += len(word) - 1 // Skip over the word that has been processed
				break
			}
		}

		// If an operation is found, store it
		for op := range operations {
			if strings.HasPrefix(str[i:], op) {
				lastOperation = op
				i += len(op) - 1 // Skip over the word "plus" or "minus"
				break
			}
		}
	}

	// Convert the result to a string representation of digits
	var result string
	if currentNum < 0 {
		result += "negative"
		currentNum = -currentNum
	}

	// Convert the final number to string representation in words
	numWords := []string{
		"zero", "one", "two", "three", "four",
		"five", "six", "seven", "eight", "nine",
	}

	for currentNum > 0 {
		digit := currentNum % 10
		result += numWords[digit]
		currentNum /= 10
	}

	// If result is empty, it means the number was zero
	if len(result) == 0 {
		result = "zero"
	}

	// Reverse the string (as we accumulated digits in reverse order)
	return reverse(result)
}

// Reverse function to reverse a string
func reverse(s string) string {
	var reversed string
	for i := len(s) - 1; i >= 0; i-- {
		reversed += string(s[i])
	}
	return reversed
}

func main() {
	// Example cases
	fmt.Println(StringExpression("onezeropluseight"))               // Output: "oneeight"
	fmt.Println(StringExpression("oneminusoneone"))                 // Output: "negativeonezero"
	fmt.Println(StringExpression("foursixminustwotwoplusonezero")) // Output: "threefour"
}
