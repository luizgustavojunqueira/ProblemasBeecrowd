inicioJ = 10
finalJ = 32

for i in range(0, 22, 2):
    for j in range(inicioJ, finalJ, 10):
        if i == 0 or i == 10 or i == 20:
            print(f"I={int(i/10)} J={int(j/10)}")
        else:
            print(f"I={i/10} J={j/10}")

    inicioJ += 2
    finalJ += 2
