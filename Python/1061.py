linha = input().split()
diaInicio = int(linha[1])
linha = input().split()
hInicio, mInicio, sInicio = int(linha[0]), int(linha[2]), int(linha[4])

linha = input().split()
diaFim = int(linha[1])
linha = input().split()
hFim, mFim, sFim = int(linha[0]), int(linha[2]), int(linha[4])

inicioEmSegundos = diaInicio * 86400 + hInicio * 3600 + mInicio * 60 + sInicio
fimEmSegundos = diaFim * 86400 + hFim * 3600 + mFim * 60 + sFim

duracaoEmSegundos =  fimEmSegundos - inicioEmSegundos

duracaoDia = duracaoEmSegundos // 86400
resto = duracaoEmSegundos % 86400
duracaoH = resto // 3600
resto = resto % 3600
duracaoM = resto // 60
resto = resto % 60
duracaoS = resto

print("{} dia(s)".format(duracaoDia))
print("{} hora(s)".format(duracaoH))
print("{} minuto(s)".format(duracaoM))
print("{} segundo(s)".format(duracaoS))