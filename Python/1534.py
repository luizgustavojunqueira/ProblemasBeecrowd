
while True:
    try:
        n = int(input())
    except EOFError:
        break

    m = []

    for i in range(n):
        m.append([])
        for j in range(n):
            if j == n-i-1:
                m[i].append(2)
            elif i == j:
                m[i].append(1)
            else:
                m[i].append(3)

    for i in range(n):
        for j in range(n):
            print(m[i][j], end="")
        print()