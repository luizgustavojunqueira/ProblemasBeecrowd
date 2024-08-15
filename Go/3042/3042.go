package main

// Está certo mas da time limit no beecrowd por algum motivo

import (
	"fmt"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {

	var m int

	fmt.Scan(&m)

	for m > 0 {

		var esq, cen, dir int
		posAtual := 2
		numToques := 0

		for i := 0; i < m; i++ {
			fmt.Scanf("%d %d %d", &esq, &cen, &dir)
			if posAtual != 1 && esq == 0 && cen == 1 && dir == 1 {
				numToques = numToques + abs(posAtual-1)
				posAtual = 1
			} else if posAtual != 2 && esq == 1 && cen == 0 && dir == 1 {
				numToques = numToques + abs(posAtual-2)
				posAtual = 2
			} else if posAtual != 3 && esq == 1 && cen == 1 && dir == 0 {
				numToques = numToques + abs(posAtual-3)
				posAtual = 3
			}
		}

		fmt.Println(numToques)

		fmt.Scan(&m)
	}

}
