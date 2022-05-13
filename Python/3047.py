m = int(input())
a = int(input())
b = int(input())

c = m - (a+b)

maiorAB = (a + b + abs(a-b)) / 2
maior = int((maiorAB + c + abs(maiorAB - c)) / 2)

print(maior)