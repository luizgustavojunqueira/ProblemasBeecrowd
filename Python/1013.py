a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)

maiorab = (a+b + abs(a-b)) / 2
maior = (maiorab + c + abs(maiorab - c)) / 2

print("{} eh o maior".format(int(maior)))