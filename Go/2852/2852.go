package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func rotate(s string, n int) string {
	return s[n:] + s[:n]
}

func main() {

	letras := "abcdefghijklmnopqrstuvwxyz"
	relacoesLetras := make([]string, 0)

	for i := 0; i < len(letras); i++ {
		relacoesLetras = append(relacoesLetras, letras)

		letras = rotate(letras, 1)
	}

	reader := bufio.NewReader(os.Stdin)

	var palavraChave string

	fmt.Scanf("%s", &palavraChave)

	var n int

	fmt.Scanf("%d", &n)

	for i := 0; i < n; i++ {

		var mensagem string

		mensagem, _ = reader.ReadString('\n')

		palavras := strings.Fields(mensagem)

		indexChave := 0
		for i, p := range palavras {

			if isVogal(string(p[0])) {

				if i == len(palavras)-1 { // last word
					fmt.Printf("%s", p)
				} else {
					fmt.Printf("%s ", p)
				}
			} else {

				palavraCifrada := ""

				for _, c := range p {

					posLetraVertical := palavraChave[indexChave] % 97
					posLetraHorizontal := c % 97

					palavraCifrada += string(relacoesLetras[posLetraVertical][posLetraHorizontal])

					if indexChave == len(palavraChave)-1 {

						indexChave = 0

					} else {

						indexChave++
					}

				}
				if i == len(palavras)-1 { // last word
					fmt.Printf("%s", palavraCifrada)
				} else {
					fmt.Printf("%s ", palavraCifrada)
				}
			}
		}

		fmt.Println()

	}

}

func isVogal(c string) bool {
	return c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
}
