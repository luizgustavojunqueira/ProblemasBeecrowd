def parse(code):
    programa = []
    p = ""
    t = len(code)
    i = 0
    while i < t:
        if code[i] != "[":
            p += code[i]
            i += 1
        else:
            programa.append(p)
            p = ""
            loop = ''
            for j in range(i, code[i+1:].index("]") + i + 2):
                loop += code[j]
            
            i += len(loop)
            programa.append(loop)

    programa.append(p)

    return programa

n = int(input())

for i in range(n):
    input()
    entrada = input()
    programa = parse(input())
    
    