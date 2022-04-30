media = 0
qntIdades = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    media += idade
    qntIdades += 1

print(f"{media/qntIdades:.2f}")