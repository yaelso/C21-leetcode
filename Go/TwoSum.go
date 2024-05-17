package main

import "fmt"

func twoSum(nums []int, target int) []int {
    values := make(map[int]int)

    for i, val := range nums {
        if index, found := values[target-val]; found {
            return []int{index, i}
        }
        values[val] = i
    }

    return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println(result) // [0, 1]
}
