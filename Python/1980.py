import math

s = input().strip()

while s != "0":

    print(math.factorial(len(s)))

    s = input().strip()