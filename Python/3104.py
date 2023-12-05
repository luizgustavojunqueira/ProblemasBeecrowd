def mod(numero, divisor):
    res = 0

    for i in range(len(numero)):
        res = (res * 10 + int(numero[i])) % divisor

    return res

a = input()
b = int(input())

print(mod(a, b))

