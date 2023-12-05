n, m = [int(i) for i in input().split()]

frutas = []
gostoFrutas = [0 for i in range(n)]

for i in range(n):
    frutas.append(input().lower())

for i in range(m):
    linha = input().lower()

    for j in range(n):
        if frutas[j] in linha or frutas[j][::-1] in linha:
            gostoFrutas[j] = 1
            break

for i in range(n):
    if gostoFrutas[i] == 1:
        print(f"Sheldon come a fruta {frutas[i]}")
    else:
        print(f"Sheldon detesta a fruta {frutas[i]}")