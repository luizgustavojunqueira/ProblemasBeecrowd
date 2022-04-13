codigo = 0
alc = 0
gas = 0
dies = 0

while codigo != 4:

    if 1 <= codigo < 4:
        if codigo == 1:
           alc += 1
        if codigo == 2:
            gas += 1
        if codigo == 3:
            dies += 1

    codigo = int(input())

print("MUITO OBRIGADO")
print(f"Alcool: {alc}")
print(f"Gasolina: {gas}")
print(f"Diesel: {dies}")