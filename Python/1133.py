x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

for i in range(x+1, y):
    x = i % 5
    if x == 2 or x == 3:
        print(i)