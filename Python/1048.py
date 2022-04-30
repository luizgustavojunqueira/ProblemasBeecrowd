sal = float(input())

aumento = 0

if 0 <= sal <= 400:
    aumento = 1.15
elif 400.01 <= sal <= 800:
    aumento = 1.12
elif 800.01 <= sal <= 1200:
    aumento = 1.10
elif 1200.01 <= sal <= 2000:
    aumento = 1.07
elif sal > 2000:
    aumento = 1.04

print("Novo salario: {:.2f}".format(sal * aumento))
print("Reajuste ganho: {:.2f}".format((sal * aumento) - sal))
print("Em percentual: {:.0f} %".format((aumento - 1) * 100))