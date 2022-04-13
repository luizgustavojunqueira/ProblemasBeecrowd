cod, qnt = input().split()
cod, qnt = int(cod), int(qnt)

cardapio = {1: 4.0, 2: 4.5, 3: 5.00, 4: 2.00, 5: 1.50}

print("Total: R$ {:.2f}".format(cardapio[cod] * qnt))