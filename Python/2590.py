def mod(numero):
    res = 0
    
    for i in range(len(numero)):
        res = (res * 10 + int(numero[i])) % 4

    return res

t = int(input())

while t:
    t -= 1
    n = input()
    
    a = mod(n)
    
    if a == 0:
        print(1)
    elif a == 1:
        print(7)
    elif a == 2:
        print(9)
    else:
        print(3)