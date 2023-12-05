alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
permutacao = input()

cripto = input()
msg = ""

for i in range(len(cripto)):
    msg += alfabeto[permutacao.index(cripto[i])]

print(msg)