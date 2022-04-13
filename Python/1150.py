x = int(input())
z = int(input())

while x >= z:
    z = int(input())

count = 0
soma = 0

while soma < z:
    soma += x
    count += 1
    x += 1

print(count)