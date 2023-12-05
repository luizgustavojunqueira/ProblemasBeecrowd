n = int(input())

copos = [0, 0, 0]

copoInicio = input()

if copoInicio == "A":
    copos[0] = 1
elif copoInicio == "B":
    copos[1] = 1
else:
    copos[2] = 1

for i in range(n):
    mov = int(input())

    if mov == 1:
        copos[0], copos[1] = copos[1], copos[0]
    elif mov == 2:
        copos[1], copos[2] = copos[2], copos[1]
    else:
        copos[0], copos[2] = copos[2], copos[0]

indexCopoFinal = copos.index(1)

if indexCopoFinal == 0:
    print("A")
elif indexCopoFinal == 1:
    print("B")
else:
    print("C")