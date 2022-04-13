while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    
    if m > n:
        aux = m
        m = n
        n = aux
    
    soma = 0

    for i in range(m, n+1):
        soma += i
        print(i, end=" ")
    print(f"Sum={soma}")