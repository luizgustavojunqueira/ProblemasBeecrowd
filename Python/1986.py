n = int(input())

letras = input().split()

res = ""

for i in range(n):
    res += chr(int(letras[i], 16))

print(res)