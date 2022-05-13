entrada = input()
jeepSituation = entrada.split()[0]
if len(entrada.split()) > 1:
    t = int(entrada.split()[1])

qntJeepSalida, qntJeepVuelta = 0, 0
tSalida, tVuelta = 0, 0

while jeepSituation != "ABEND":
    if jeepSituation == "SALIDA":
        qntJeepSalida += 1
        tSalida += t
    else:
        qntJeepVuelta += 1
        tVuelta += t

    entrada = input()
    jeepSituation = entrada.split()[0]
    if len(entrada.split()) > 1:
        t = int(entrada.split()[1])

print(tSalida - tVuelta)
print(qntJeepSalida - qntJeepVuelta)