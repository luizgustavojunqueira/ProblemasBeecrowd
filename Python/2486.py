t = int(input())

while t > 0:

    totalMg = 0

    for i in range(t):
        qnt, alimento = input().split(" ", 1)
        qnt = int(qnt)

        if alimento == "suco de laranja":
            totalMg += qnt * 120
        elif alimento == "morango fresco" or alimento == "mamao":
            totalMg += qnt * 85
        elif alimento == "goiaba vermelha":
            totalMg += qnt * 70
        elif alimento == "manga":
            totalMg += qnt * 56
        elif alimento == "laranja":
            totalMg += qnt * 50
        elif alimento == "brocolis":
            totalMg += qnt * 34

    
    if totalMg < 110:
        print(f"Mais {110 - totalMg} mg")
    elif totalMg > 130:
        print(f"Menos {totalMg - 130} mg")
    else:
        print(f"{totalMg} mg")



    t = int(input())