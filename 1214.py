c = int(input())

for i in range(c):
    qnt, notas = input().split(" ", 1)
    qnt = int(qnt)

    notas = list(map(int, notas.split()))

    media = sum(notas)
    media = media / qnt

    qntAcima = 0

    for n in notas:
        if n > media:
            qntAcima += 1

    percent = qntAcima * 100 / qnt;

    print(f"{percent:.3f}%")