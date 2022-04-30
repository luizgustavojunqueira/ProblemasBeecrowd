l, c = map(int, input().split())

m = []

for i in range(l):
    m.append(list(map(int, input().split())))

stop = False
posx = 0
posy = 0

for i in range(1, l-1):
    for j in range(1, c-1):
        if m[i][j] == 42 and 7 == m[i-1][j] == m[i+1][j] == m[i][j-1] == m[i][j+1] == m[i-1][j-1] == m[i-1][j+1] == m[i+1][j-1] == m[i+1][j+1]:
            posx = i + 1
            posy = j + 1
            stop = True
            break
    if stop:
        break

print(f"{posx} {posy}")