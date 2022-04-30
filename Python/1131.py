continuar = 1
total_grenais = 0
vitorias_Gremio = 0
vitorias_Inter = 0
empates = 0

while continuar != 2:

    if continuar == 1:
        inter, gremio = map(int, input().split())
        total_grenais += 1
        if inter > gremio:
            vitorias_Inter += 1
        elif gremio > inter:
            vitorias_Gremio += 1
        else:
            empates += 1


    continuar = int(input("Novo grenal (1-sim 2-nao)\n"))

print(f"{total_grenais} grenais")
print(f"Inter:{vitorias_Inter}")
print(f"Gremio:{vitorias_Gremio}")
print(f"Empates:{empates}")

if vitorias_Gremio > vitorias_Inter:
    print("Gremio venceu mais")
elif vitorias_Gremio < vitorias_Inter:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")