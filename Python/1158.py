n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())

    soma = 0
    count = 0
    while count != y:
        if x % 2 != 0:
            soma += x
            count += 1
        x += 1

    print(soma)