a1 = int(input())
a2 = int(input())
a3 = int(input())

tempo1Andar = 2 * a2 + 4 * a3
tempo2Andar = 2 * a1 + 2 * a3
tempo3Andar = 4 * a1 + 2 * a2 

tempos = [tempo1Andar, tempo2Andar, tempo3Andar]

menor = 10000

for tempo in tempos:
    if tempo < menor:
        menor = tempo

print(menor)