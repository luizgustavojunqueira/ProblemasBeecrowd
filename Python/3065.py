m = int(input())
teste = 0

while m != 0:

    teste += 1

    exp = input()

    numeros = exp.replace('+', ' ').replace('-', ' ').split()

    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])

    sinais = []

    for i in range(len(exp)):
        if exp[i] == "+" or exp[i] == "-":
            sinais.append(exp[i])

    res = numeros[0]

    for i in range(len(sinais)):
        if sinais[i] == "+":
            res += numeros[i+1]
        else:
            res -= numeros[i+1]

    print(f"Teste {teste}")
    print(res)
    print()

    m = int(input())