dec = int(input())

valoresConversao = ['A', 'B', 'C', 'D', 'E', 'F']
restosDivisoes = []

while dec > 0:
    resto = dec % 16
    dec = dec // 16
    restosDivisoes.append(resto)

resultado = ''

for i in range(len(restosDivisoes)):
    if restosDivisoes[i] >= 10:
        resultado += valoresConversao[restosDivisoes[i] - 10]
    else:
        resultado += str(restosDivisoes[i])
    
print(resultado[::-1])