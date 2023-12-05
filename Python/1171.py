n = int(input())

entradaNumeros = []
frequenciaNumeros = {}

for i in range(n):
    x = int(input())
    entradaNumeros.append(x)

    if x in frequenciaNumeros:
        frequenciaNumeros[x] += 1
    else:
        frequenciaNumeros[x] = 1

for k, v in dict(sorted(frequenciaNumeros.items())).items():
    print(f"{k} aparece {v} vez(es)")