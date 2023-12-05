def pegarMaiorNota(notas):
    maior = 0 
    for n in notas:
        if n > maior:
            maior = n
    return maior

def qntPessoasPorNota(notas, nota):
    qnt = 0
    for n in notas:
        if n == nota:
            qnt += 1
    return qnt

def removerMaioresNotas(notas, nota):
    while nota in notas:
        for n in notas:
            if n == nota:
                notas.pop(notas.index(n))
                break
    return notas

n = int(input())
k = int(input())

notas = []
qntClassificados = 0

for i in range(n):
    notas.append(int(input()))

while qntClassificados < k:
    maiorNota = pegarMaiorNota(notas)
    qntClassificados += qntPessoasPorNota(notas, maiorNota)
    notas = removerMaioresNotas(notas, maiorNota)


print(qntClassificados)