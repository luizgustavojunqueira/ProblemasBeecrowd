n = int(input())
inicio = 1
fim = 4

for i in range(0, n):
    for j in range(inicio, fim):
        print(j, end=" ")
    print("PUM")
    inicio += 4
    fim += 4