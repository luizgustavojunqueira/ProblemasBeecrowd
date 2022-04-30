n = int(input())

totalSaque = 0
totalSaqueAcerto = 0
totalBloqueio = 0
totalBloqueioAcerto = 0
totalAtaque = 0
totalAtaqueAcerto = 0

for i in range(n):
    nome = input()
    s, b, a = map(int, input().split())
    s1, b1, a1 = map(int, input().split())

    totalSaque += s
    totalSaqueAcerto += s1
    totalBloqueio += b
    totalBloqueioAcerto += b1
    totalAtaque += a
    totalAtaqueAcerto += a1

print(f"Pontos de Saque: {((totalSaqueAcerto*100) / totalSaque):.2f} %")
print(f"Pontos de Bloqueio: {((totalBloqueioAcerto*100) / totalBloqueio):.2f} %")
print(f"Pontos de Ataque: {((totalAtaqueAcerto*100) / totalAtaque):.2f} %")