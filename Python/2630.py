t = int(input())

for i in range(t):

    conversao = input()
    r, g, b = map(int, input().split())
    rgb = [r, g, b]
    p = 0

    if conversao == "eye":
        p = 0.3 * r + 0.59 * g + 0.11 * b
    elif conversao == "mean":
        p = (r+g+b) / 3
    elif conversao == "max":
        for v in rgb:
            if v > p:
                p = v

    elif conversao == "min":
        p = 256
        for v in rgb:
            if v < p:
                p = v
        


    print(f"Caso #{i+1}: {int(p)}")