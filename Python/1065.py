numPares = 0

for i in range(0, 5):
    if int(input()) % 2 == 0:
        numPares += 1
print(f"{numPares} valores pares")