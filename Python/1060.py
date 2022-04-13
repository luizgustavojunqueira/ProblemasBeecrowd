numPositivos = 0
for i in range(0,6):
    if float(input()) > 0:
        numPositivos += 1
print("{} valores positivos".format(numPositivos))