n = int(input())

g, u = 0, 0

for i in range(n):
    c, v = input().split()
    v = int(v)

    if c == "V":
        g += v
    else:
        u += v

if g < u:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")