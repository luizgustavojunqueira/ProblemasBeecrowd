package main

import (
	"fmt"
)

func main() {

	var f, s, g, u, d int

	fmt.Scan(&f, &s, &g, &u, &d)

	numApertos := 0

	andaresVisitados := make(map[int]bool)

	for i := 0; i < f; i++ {
		andaresVisitados[i] = false
	}

	andaresVisitados[s-1] = true

	for s != g {
		if s < g {
			s += u
			numApertos++
		} else if s > g {
			s -= d
			numApertos++
		}

		if s == g {
			break
		}

		if andaresVisitados[s-1] {
			fmt.Println("use the stairs")
			return
		}

		andaresVisitados[s-1] = true

	}

	fmt.Println(numApertos)

}
