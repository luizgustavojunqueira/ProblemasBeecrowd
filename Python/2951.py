n, g = map(int, input().split())

runes = {}

for i in range(n):
    r, v = input().split()
    v = int(v)

    runes[r] = v

totalRecitadas = int(input())

recitadas = list(input().split())

fTotal = 0

for r in recitadas:
    fTotal += runes[r]

print(fTotal)

if fTotal >= g:
    print("You shall pass!")
else:
    print("My precioooous")