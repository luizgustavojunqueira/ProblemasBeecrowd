lista = []

while True:
    try:
        lista.append(input())
    except EOFError:
        break

lista = set(lista)
print(len(lista))

## Também funciona mas é mais lento

# listaUnicos = []

# for i in range(len(lista)):
#     if not lista[i] in listaUnicos:
#         listaUnicos.append(lista[i])

# print(len(listaUnicos))