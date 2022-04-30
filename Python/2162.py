n = int(input())
alturas = list(map(int, input().split()))
mesmoPadrao = 0

if n == 1:
    mesmoPadrao = 1
elif n == 2:
    if alturas[0] != alturas[1]:
        mesmoPadrao = 1
    else:
        mesmoPadrao = 0
else:
    for i in range(1, n):
        if alturas[0] > alturas[1]:
            if i % 2 != 0:
                if alturas[i] < alturas[i-1]:
                    mesmoPadrao = 1
                else:
                    mesmoPadrao = 0
                    break
            elif alturas[i] > alturas[i-1]:
                mesmoPadrao = 1
            else:
                mesmoPadrao = 0
                break

        elif alturas[0] < alturas[1]:
            if i % 2 != 0:
                if alturas[i] > alturas[i-1]:
                    mesmoPadrao = 1
                else:
                    mesmoPadrao = 0
                    break
            elif alturas[i] < alturas[i-1]:
                mesmoPadrao = 1
            else:
                mesmoPadrao = 0
                break
        
print(mesmoPadrao)
