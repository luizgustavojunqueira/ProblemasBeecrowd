t = int(input())

for i in range(0, t):
    entrada = input().split()
    popA, popB = int(entrada[0]), int(entrada[1])
    gA, gB = float(entrada[2]), float(entrada[3])

    anos = 0

    while popA <= popB:
        crescA = int(popA * (gA/100))
        crescB = int(popB * (gB/100))
        popA += crescA
        popB += crescB
        anos += 1
        if anos > 100:
            print("Mais de 1 seculo.")
            break
    
    if anos <= 100:
        print(f"{anos} anos.")