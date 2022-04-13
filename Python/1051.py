sal = float(input())

imposto = 0

if 2000.01 <= sal <= 3000:
    imposto = (sal - 2000) * 0.08
elif 3000.01 <= sal <= 4500:
    imposto = (sal - 3000) * 0.18 + 1000 * 0.08
elif sal > 4500:
    imposto = (sal - 4500) * 0.28 + (1500 * 0.18)  + (1000 * 0.08)


if imposto == 0:
    print("Isento")
else:
    print("R$ {:.2f}".format(imposto))