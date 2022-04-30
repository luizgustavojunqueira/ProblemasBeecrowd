numPiscadas = 0
soma = 0

while numPiscadas < 3:

    entrada = input()

    if entrada == "caw caw":
        print(soma)
        soma = 0
        numPiscadas += 1
    else:
        digitos = [] 
        for i in range(3):
            if entrada[i] == "-":
                digitos.append(0)
            else:
                digitos.append(1)
        
        soma += digitos[0] * 4 + digitos[1] * 2 + digitos[2]