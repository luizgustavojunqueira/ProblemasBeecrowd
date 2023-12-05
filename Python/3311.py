n = int(input())

ficha = []

for i in range(n):
    ficha.append(input())

ficha.sort(key= lambda x: x[0])

for f in ficha:
    print(f)