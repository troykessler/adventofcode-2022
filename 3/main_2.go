package main

import (
	"fmt"
	"github.com/troykessler/adventofcode-2022/utils"
	"strings"
)

func unique(input string) (uniques string) {
	uniqueMap := make(map[string]bool)

	for _, c := range strings.Split(input, "") {
		uniqueMap[c] = true
	}

	for key := range uniqueMap {
		uniques += key
	}

	return
}

func main() {
	content := strings.Split(utils.ReadContent("./3/inputs.txt"), "\n")

	score := 0
	itemPriorities := [52]string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

	rucksackGroups := make([][]string, 0)
	current := make([]string, 0)

	for index, rucksack := range content {

		current = append(current, unique(rucksack))

		if (index+1)%3 == 0 {
			rucksackGroups = append(rucksackGroups, current)
			current = make([]string, 0)
		}
	}

	for _, group := range rucksackGroups {
		badges := make(map[string]int)

		for _, rucksack := range group {
			for _, c := range strings.Split(rucksack, "") {
				if _, exists := badges[c]; exists {
					badges[c]++

					if badges[c] == 3 {
						for index, item := range itemPriorities {
							if item == c {
								score += index + 1
							}
						}
					}
				} else {
					badges[c] = 1
				}
			}
		}
	}

	fmt.Println(score)
}
