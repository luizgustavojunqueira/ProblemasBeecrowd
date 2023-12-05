o, b, i = map(float, input().split())

if o < b and (o < i or b <= i):
    print("Otavio")
elif b < o and (b < i or o <= i):
    print("Bruno")
elif i < b and (i < o or b <= o):
    print("Ian")
else:
    print("Empate")
