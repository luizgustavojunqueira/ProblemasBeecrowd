t = int(input())
suposicoes = input().split()

acertos = 0

for i in range(5):
    suposicoes[i] = int(suposicoes[i])
    if suposicoes[i] == t:
        acertos += 1

print(acertos)