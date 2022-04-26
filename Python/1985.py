qntProdutos = int(input())

precos = {1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5}
precoFinal = 0

for i in range(qntProdutos):
    codigo, qnt = map(int, input().split())
    precoFinal += qnt * precos[codigo]

print(f"{precoFinal:.2f}")
