n = int(input())

convidados = input().split()

qntParticipantes = 0

for i in range(len(convidados)):
    if convidados[i] == "1":
        qntParticipantes += 1

print(qntParticipantes)