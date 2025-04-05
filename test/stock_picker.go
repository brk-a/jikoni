package main

import "fmt"

// StockPicker function to calculate the maximum profit
func StockPicker(arr []int) int {
    // Ensure the array has at least two elements
    if len(arr) < 2 {
        return -1
    }

    // Initialize the minimum price to the first element
    var minPrice = arr[0]
    var maxProfit = -1  // Start with -1 to handle no profit case

    // Loop through the stock prices
    for i := 1; i < len(arr); i++ {
        // Calculate the potential profit if sold on day i
        varOcg := arr[i] - minPrice

        // Update the max profit if the current profit is greater
        if varOcg > maxProfit {
            maxProfit = varOcg
        }

        // Update the minimum price if a new lower price is found
        if arr[i] < minPrice {
            minPrice = arr[i]
        }
    }

    // Return the maximum profit found, or -1 if no profit was possible
    return maxProfit
}

func main() {
    // Example cases
    fmt.Println(StockPicker([]int{10, 12, 4, 5, 9}))           // Output: 5
    fmt.Println(StockPicker([]int{14, 20, 4, 12, 5, 11}))     // Output: 8
    fmt.Println(StockPicker([]int{44, 30, 24, 32, 35, 30, 40, 38, 15})) // Output: 16
    fmt.Println(StockPicker([]int{10, 9, 8, 2}))              // Output: -1
}
