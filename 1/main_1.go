package main

import (
	"fmt"
	"github.com/troykessler/adventofcode-2022/utils"
	"sort"
	"strconv"
	"strings"
)

func main() {
	content := strings.Split(utils.ReadContent("./1/inputs.txt"), "\n")

	results := make([]int, 0)
	current := 0

	for _, c := range content {
		if c == "" {
			results = append(results, current)
			current = 0
		} else if n, err := strconv.ParseInt(c, 10, 64); err == nil {
			current += int(n)
		}
	}

	results = append(results, current)

	sort.Sort(sort.Reverse(sort.IntSlice(results)))

	fmt.Println(results[0])
}
