n = int(input())

for i in range(n):
    input()
    entrada = input()
    codigo = input()

    vetor = [0 for i in range(30000)]

    ponteiro = 0
    iteratorEntrada = 0

    i = 0

    while i < len(codigo):
        if codigo[i] == ">":
            ponteiro += 1
        elif codigo[i] == "<":
            ponteiro -= 1
        elif codigo[i] == "+":
            vetor[ponteiro] += 1    
        elif codigo[i] == "-":
            vetor[ponteiro] -= 1
        elif codigo[i] == ".":
            print(chr(vetor[ponteiro]), end = "")
        elif codigo[i] == ",":
            if iteratorEntrada < len(entrada):
                vetor[ponteiro] = ord(entrada[iteratorEntrada])
                iteratorEntrada += 1
        elif codigo[i] == "#":
            for j in range(10):
                print(chr(vetor[j]), end = " ")
            print()
        elif codigo[i] == "[":
            if vetor[ponteiro] == 0:
                colcheteAberto = 1
                while colcheteAberto > 0:
                    i += 1
                    if codigo[i] == '[':
                        colcheteAberto += 1
                    elif codigo[i] == ']':
                        colcheteAberto -= 1
        elif codigo[i] == "]":
            colcheteAberto = 1
            while colcheteAberto > 0:
                i -= 1
                if codigo[i] == '[':
                    colcheteAberto -= 1
                elif codigo[i] == ']':
                    colcheteAberto += 1

            i -= 1
        
        i += 1