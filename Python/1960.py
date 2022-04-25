n = int(input())

def getValorDecimalMaxELetra(x):
    if x - 1000 >= 0:
        return [1000, "M"]
    elif x - 900 >= 0:
        return [900, "CM"]
    elif x - 500 >= 0:
        return [500, "D"]
    elif x - 400 >= 0:
        return [400, "CD"]
    elif x - 100 >= 0:
        return [100, "C"]
    elif x - 90 >= 0:
        return [90, "XC"]
    elif x - 50 >= 0:
        return [50, "L"]
    elif x - 40 >= 0:
        return [40, "XL"]
    elif x - 10 >= 0:
        return [10, "X"]
    elif x - 9 >= 0:
        return [9, "IX"]
    elif x - 5 >= 0:
        return [5, "V"]
    elif x - 4 >= 0:
        return [4, "IV"]
    else:
        return [1, "I"]

valorDecimalMax, letra = getValorDecimalMaxELetra(n)
res = ""

while n >= 1:
    n = n - valorDecimalMax
    res += letra
    valorDecimalMax, letra = getValorDecimalMaxELetra(n)

print(res)