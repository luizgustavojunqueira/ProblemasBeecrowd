n, c = [int(i) for i in input().split()]

pessoasNoElevador = 0
excedeu = False

for i in range(n):
    s, e = [int(i) for i in input().split()]

    pessoasNoElevador += -s + e

    if pessoasNoElevador > c:
        excedeu = True

if excedeu:
    print("S")
else:
    print("N")