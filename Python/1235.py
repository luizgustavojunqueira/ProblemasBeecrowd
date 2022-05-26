n = int(input())

for i in range(n):
    msg = input()
    posMeio = int(len(msg) / 2)
    metade1, metade2 = msg[:posMeio], msg[posMeio:]
   
    print(metade1[::-1] + metade2[::-1])
