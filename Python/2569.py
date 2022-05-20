a, op, b = input().replace("7", "0").split()
a = int(a)
b = int(b)

res = 0

if op == "+":
    res = a + b
else:
    res = a * b

res = str(res).replace("7", "0")

print(int(res))