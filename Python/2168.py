n = int(input())

m =  []

for i in range(n+1):
    m.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        soma = m[i][j] + m[i][j+1] + m[i+1][j] + m[i+1][j+1]
        if soma >= 2:
            print("S", end="")
        else:
            print("U", end="")
    print()