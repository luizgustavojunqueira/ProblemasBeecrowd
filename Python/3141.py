nome = input()

dia, mes, ano = map(int, input().split("/"))
diaNasc, mesNasc, anoNasc = map(int, input().split("/"))

if dia == diaNasc and mes == mesNasc:
    print("Feliz aniversario!")

d = (mes - mesNasc) * 31 + dia - diaNasc

if d >= 0:
    print(f"Voce tem {ano - anoNasc} anos {nome}.")
else:
    print(f"Voce tem {ano - anoNasc - 1} anos {nome}.")
