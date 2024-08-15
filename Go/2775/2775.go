package main

import (
	"fmt"
)

func main() {
	var n int

	_, err := fmt.Scanf("%d", &n)

	for err == nil {

		pacotes, tempos := make([]int, n), make([]int, n)

		for i := 0; i < n; i++ {
			fmt.Scanf("%d", &pacotes[i])
		}

		for i := 0; i < n; i++ {
			fmt.Scanf("%d", &tempos[i])
		}

		soma := 0
		alterado := true

		for alterado {
			alterado = false
			for i := 0; i < n-1; i++ {
				if pacotes[i] > pacotes[i+1] {
					soma += tempos[i] + tempos[i+1]
					pacotes[i], pacotes[i+1] = pacotes[i+1], pacotes[i]
					tempos[i], tempos[i+1] = tempos[i+1], tempos[i]
					alterado = true
				}
			}
		}

		fmt.Println(soma)

		_, err = fmt.Scanf("%d", &n)

	}
}
