n = int(input())

c, t = 0, 0
extraC, extraT = 0, 0

for i in range(n):
    casa, trabalho = input().split()

    if casa == "chuva" and extraC == 0:
        c += 1
        extraT += 1
    elif casa == "chuva" and extraC > 0:
        extraC -= 1
        extraT += 1
    
    if trabalho == "chuva" and extraT == 0:
        t += 1
        extraC += 1
    elif trabalho == "chuva" and extraT > 0:
        extraT -= 1
        extraC += 1


print(c, t)