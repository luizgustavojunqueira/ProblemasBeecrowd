package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int

	fmt.Scan(&n)

	for n > 0 {

		x := make([]int, 2*n)

		for i := 0; i < 2*n; i++ {
			fmt.Scan(&x[i])
		}

		sort.Ints(x)

		maior := x[n-1] + x[n]
		menor := maior

		for i := 0; i < n; i++ {
			b := x[i] + x[2*n-1-i]
			if b < menor {
				menor = b
			} else if b > maior {
				maior = b
			}

		}

		fmt.Println(maior, menor)

		fmt.Scan(&n)
	}
}
