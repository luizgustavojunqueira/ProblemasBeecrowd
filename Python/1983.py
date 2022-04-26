n = int(input())

maiorNota = 0
matriculaMaiorNota = 0

for i in range(n):
    matricula, nota = input().split()
    matricula, nota = int(matricula), float(nota)
    if nota > maiorNota:
        maiorNota = nota
        matriculaMaiorNota = matricula

if maiorNota >= 8:
    print(matriculaMaiorNota)
else:
    print("Minimum note not reached")