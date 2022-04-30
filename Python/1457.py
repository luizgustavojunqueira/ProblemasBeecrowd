t = int(input())

for u in range(0, t):
    entrada = input()
    n, k = entrada.split("!", 1)
    n = int(n)
    k = k + "!"
    k = k.count("!")
    total = 1
    for i in range(n, 1, -k):
        total *= i
    print(total)