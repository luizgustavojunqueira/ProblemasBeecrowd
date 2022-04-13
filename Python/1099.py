n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())

    if x > y:
        aux = x
        x = y
        y = aux

    soma = 0

    for num in range(x + 1, y):
        if num % 2 != 0:
            soma += num
    print(soma)