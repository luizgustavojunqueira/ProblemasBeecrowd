vPar = []
vImpar = []

for i in range(0, 15):
    x = int(input())

    if x % 2 == 0:
        if len(vPar) < 5:
            vPar.append(x)
        else:
            for j in range(len(vPar)):
                print(f"par[{j}] = {vPar[j]}")
            vPar = [x]

    else:
        if len(vImpar) < 5:
            vImpar.append(x)
        else:
            for j in range(len(vImpar)):
                print(f"impar[{j}] = {vImpar[j]}")
            vImpar = [x]

for i in range(len(vImpar)):
    print(f"impar[{i}] = {vImpar[i]}")

for i in range(len(vPar)):
    print(f"par[{i}] = {vPar[i]}")
    