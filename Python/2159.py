from math import log

n = int(input())

minimo = n / log(n)
maximo = 1.25506 * minimo

print(f"{minimo:.1f} {maximo:.1f}")