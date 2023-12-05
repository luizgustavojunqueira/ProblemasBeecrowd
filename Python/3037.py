n = int(input())

for i in range(n):

    pJoao = 0
    pMaria = 0

    for j in range(3):  
        x, d = map(int, input().split())
        pJoao += x*d
    for j in range(3):  
        x, d = map(int, input().split())
        pMaria += x*d    

    if pMaria > pJoao:
        print("MARIA")
    else:
        print("JOAO")