seg = int(input())

horas = seg // 3600
resto = seg % 3600
minutos = resto // 60
resto = resto % 60
seg = resto

print("{}:{}:{}".format(horas, minutos, seg))