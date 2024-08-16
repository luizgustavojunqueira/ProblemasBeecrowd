package main

import (
	"fmt"
	"math"
)

func main() {

	var n int

	fmt.Scan(&n)

	naves := make([][3]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&naves[i][0], &naves[i][1], &naves[i][2])
	}

	var dist int

	for i := 0; i < n; i++ {
		menorDistancia := 200000

		for j := 0; j < n; j++ {
			if i != j {
				dist = int(math.Sqrt(math.Pow(float64(naves[i][0]-naves[j][0]), 2) + math.Pow(float64(naves[i][1]-naves[j][1]), 2) + math.Pow(float64(naves[i][2]-naves[j][2]), 2)))

				if dist < menorDistancia {
					menorDistancia = dist
				}
			}

		}
		if menorDistancia < 20 {
			fmt.Println("A")
		} else if menorDistancia < 50 {
			fmt.Println("M")
		} else {
			fmt.Println("B")
		}
	}

}
