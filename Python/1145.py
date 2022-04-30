x, y = map(int, input().split())

for i in range(1, y, x):
    for j in range(i, i+x):
        if j == i + x - 1:
            print(j)
        else:
            print(j, end=" ")