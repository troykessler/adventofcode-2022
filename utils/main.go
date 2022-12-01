package utils

import "os"

func ReadContent(path string) string {
	content, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	return string(content)
}
