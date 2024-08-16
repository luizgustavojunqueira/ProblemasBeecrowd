package main

import (
	"fmt"
	"sort"
)

func main() {

	var N, P int

	_, err := fmt.Scan(&N, &P)

	for err == nil {

		k1 := ((N + 1) / 4) - 2
		k3 := (3 * (N + 1) / 4) - 1

		if k1 < 0 {
			k1 = 0
		}

		pesos := make([]float64, N)

		for i := 0; i < N; i++ {
			fmt.Scan(&pesos[i])
		}

		sort.Float64s(pesos)

		q1 := pesos[k1] + (0.25*float64(N+1)-float64(k1))*(pesos[k1+1]-pesos[k1])
		q3 := pesos[k3] + (0.75*float64(N+1)-float64(k3))*(pesos[k3+1]-pesos[k3])

		a := q1 - 0.5*(q3-q1)
		b := q3 + 0.5*(q3-q1)

		x, y := 0, 0

		// Pega a quantidade de elementos menores ou iguais que a
		for i := 0; i < N; i++ {
			if pesos[i] < a {
				x++
			}
		}

		// Pega a quantidade de elementos maiores ou iguais que b
		for i := 0; i < N; i++ {
			if pesos[i] > b {
				y++
			}
		}

		z := (x + y) * P

		fmt.Println(z)

		_, err = fmt.Scan(&N, &P)

	}

}
