def fibonot(k):
    anterior = 1
    atual = 2
    proximo = 3
    while k > 0:
        # Anda pela sequencia de fibonacci até que k seja negativo
        anterior = atual
        atual = proximo
        proximo = anterior + atual

        #Subtrai o anterior - 1 de k
        k -= (anterior - 1)

    #Soma novamente o anterior e subtrai 1
    k += (anterior - 1)

    return atual + k

k = int(input())
print(fibonot(k))