package main

import (
	"fmt"
	"github.com/troykessler/adventofcode-2022/utils"
	"strings"
)

func main() {
	content := strings.Split(utils.ReadContent("./3/inputs.txt"), "\n")

	score := 0
	itemPriorities := [52]string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

	for _, rucksack := range content {
		var item string

		compartment1 := make([]string, 0)
		compartment2 := make([]string, 0)

		for index, item := range strings.Split(rucksack, "") {
			if index < len(rucksack)/2 {
				compartment1 = append(compartment1, item)
			} else {
				compartment2 = append(compartment2, item)
			}
		}

		for _, i := range compartment1 {
			for _, e := range compartment2 {
				if i == e {
					item = i
					break
				}
			}
		}

		for priority, value := range itemPriorities {
			if item == value {
				score += priority + 1
				break
			}
		}

	}

	fmt.Println(score)
}
