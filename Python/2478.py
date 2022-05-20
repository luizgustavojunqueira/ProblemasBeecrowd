x = int(input())

nomeESugestoes = {}

for i in range(x):
    entrada = input().split()
    nome = entrada[0]
    sugestoes = entrada[1:]

    nomeESugestoes[nome] = sugestoes

while True:
    try:

        nome, presente = input().split()

        if nome in nomeESugestoes:
            if presente in nomeESugestoes[nome]:
                print("Uhul! Seu amigo secreto vai adorar o/")
            else:
                print("Tente Novamente!")
        else:
            print("Tente Novamente!")

    except EOFError:
        break