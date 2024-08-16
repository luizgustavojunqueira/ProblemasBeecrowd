package main

import (
	"fmt"
	"sort"
)

func main() {

	var n, x, p, m, g int

	fmt.Scan(&n, &x)

	var titas string
	fmt.Scan(&titas)

	fmt.Scan(&p, &m, &g)

	muralhas := make([]int, 2*n)

	for i := 0; i < 2*n; i++ {
		muralhas[i] = x
	}

	t1, t2, t3 := 1, 1, 1

	for i := 0; i < n; i++ {
		switch titas[i] {
		case 'P':
			for muralhas[t1] < p {
				t1++
			}
			muralhas[t1] -= p
		case 'M':
			for muralhas[t2] < m {
				t2++
			}
			muralhas[t2] -= m
		case 'G':
			for muralhas[t3] < g {
				t3++
			}
			muralhas[t3] -= g
		}
	}

	res := []int{t1, t2, t3}

	sort.Ints(res)

	fmt.Println(res[2])

}
