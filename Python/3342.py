n = int(input())
n = n*n

nPretas = int(n/2)
nBrancas = 0

if n % 2 == 0:
    nBrancas = nPretas
else:
    nBrancas = int((n+1) / 2)

print(f"{nBrancas} casas brancas e {nPretas} casas pretas")