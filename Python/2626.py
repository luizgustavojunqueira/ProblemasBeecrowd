while True:
    try:
        j1, j2, j3 = input().split()

        if j1 == j3 and (j2 == "papel" and j1 == "pedra" or j2 == "pedra" and j1 == "tesoura" or j2 == "tesoura" and j1 == "papel"):
                print("Iron Maiden's gonna get you, no matter how far!")
        elif j1 == j2 and (j3 == "papel" and j1 == "pedra" or j3 == "pedra" and j1 == "tesoura" or j3 == "tesoura" and j1 == "papel"):
                print("Urano perdeu algo muito precioso...")
        elif j3 == j2 and (j1 == "papel" and j2 == "pedra" or j1 == "pedra" and j2 == "tesoura" or j1 == "tesoura" and j2 == "papel"):
                print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")

    except EOFError:
        break