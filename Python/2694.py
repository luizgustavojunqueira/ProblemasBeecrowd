n = int(input())

for i in range(n):
    e = input()

    numeros = []
    num = 0

    for j in range(len(e)):
        if e[j].isdigit():
            num = num * 10 + int(e[j])
        elif num > 0:
            numeros.append(num)
            num = 0

    numeros.append(num)

    print(sum(numeros))