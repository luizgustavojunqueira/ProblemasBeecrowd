n = float(input())

n = n * 100

nota100 = n // 10000
resto = n % 10000
nota50 = resto // 5000
resto = resto % 5000
nota20 = resto // 2000
resto = resto % 2000
nota10 = resto // 1000
resto = resto % 1000
nota5 = resto // 500
resto = resto % 500
nota2 = resto // 200
resto = resto % 200

moeda1 = resto // 100
resto = resto % 100
moeda50Cents = resto // 50
resto = resto % 50
moeda25Cents = resto // 25
resto = resto % 25
moeda10Cents = resto // 10
resto = resto % 10
moeda5Cents = resto // 5
resto = resto % 5
moeda1Cents = resto 

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(nota100)))
print("{} nota(s) de R$ 50.00".format(int(nota50)))
print("{} nota(s) de R$ 20.00".format(int(nota20)))
print("{} nota(s) de R$ 10.00".format(int(nota10)))
print("{} nota(s) de R$ 5.00".format(int(nota5)))
print("{} nota(s) de R$ 2.00".format(int(nota2)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(moeda1)))
print("{} moeda(s) de R$ 0.50".format(int(moeda50Cents)))
print("{} moeda(s) de R$ 0.25".format(int(moeda25Cents)))
print("{} moeda(s) de R$ 0.10".format(int(moeda10Cents)))
print("{} moeda(s) de R$ 0.05".format(int(moeda5Cents)))
print("{} moeda(s) de R$ 0.01".format(int(moeda1Cents)))