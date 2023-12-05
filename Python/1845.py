maior = 'BJPSVXZ'
menor = 'bjpsvxz'

while True:
    try:
        c = input()
        res = ''
        
        for i in range(len(c)):
            if c[i] in maior:
                res += 'F'
            elif c[i] in menor:
                res += 'f'
            else:
                res += c[i]

        print(res)
        
    except EOFError:
        break