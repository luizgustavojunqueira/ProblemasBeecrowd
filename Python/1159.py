x = -1

while x != 0:

    x = int(input())

    if x == 0:
        break 

    count = 0
    soma = 0

    while count < 5:
        if x % 2 == 0:
            soma += x
            count += 1
        x += 1
        
    print(soma)