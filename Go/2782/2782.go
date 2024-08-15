package main

import (
	"fmt"
)

func main() {
	var n int

	fmt.Scanf("%d", &n)

	if n <= 2 {
		fmt.Println(1)
		return
	}

	qnt := 1

	v := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &v[i])
	}

	for i := 0; i < n-2; i++ {
		if (v[i] - v[i+1]) != (v[i+1] - v[i+2]) {
			qnt++
		}
	}

	fmt.Println(qnt)

}
