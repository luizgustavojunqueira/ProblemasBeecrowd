valPar, valImpar, valPos, valNeg = 0, 0, 0, 0

for i in range(0, 5):
    x = int(input())
    if x > 0 :
        valPos += 1
    if x < 0:
        valNeg += 1
    if x % 2 == 0:
        valPar += 1
    else:
        valImpar += 1

print(f"{valPar} valor(es) par(es)")
print(f"{valImpar} valor(es) impar(es)")
print(f"{valPos} valor(es) positivo(s)")
print(f"{valNeg} valor(es) negativo(s)")