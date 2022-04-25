t = int(input())

for i in range(t):
    j1, j2 = input().split()

    if j1 == j2:
        print(f"Caso #{i+1}: De novo!")
    elif j1 == "tesoura" and j2 == "papel":
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "papel" and j2 == "pedra":
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "pedra" and j2 == "lagarto": 
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "lagarto" and j2 == "Spock": 
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "Spock" and j2 == "tesoura": 
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "tesoura" and j2 == "lagarto":
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "lagarto" and j2 == "papel": 
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "papel" and j2 == "Spock": 
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "Spock" and j2 == "pedra": 
        print(f"Caso #{i+1}: Bazinga!")
    elif j1 == "pedra" and j2 == "tesoura": 
        print(f"Caso #{i+1}: Bazinga!")
    else:
        print(f"Caso #{i+1}: Raj trapaceou!")