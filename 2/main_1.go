package main

import (
	"fmt"
	"github.com/troykessler/adventofcode-2022/utils"
	"strings"
)

func main() {
	content := strings.Split(utils.ReadContent("./2/inputs.txt"), "\n")

	score := 0

	opponentValues := make(map[string]int)
	opponentValues["A"] = 1 // rock
	opponentValues["B"] = 2 // paper
	opponentValues["C"] = 3 // scissor

	shapeValues := make(map[string]int)
	shapeValues["X"] = 1 // rock
	shapeValues["Y"] = 2 // paper
	shapeValues["Z"] = 3 // scissor

	for _, round := range content {
		if opponentValues[string(round[0])]%3 == shapeValues[string(round[2])]%3 {
			score += 3 + shapeValues[string(round[2])]
		} else if (opponentValues[string(round[0])]+1)%3 == shapeValues[string(round[2])]%3 {
			score += 6 + shapeValues[string(round[2])]
		} else {
			score += 0 + shapeValues[string(round[2])]
		}
	}

	fmt.Println(score)
}
