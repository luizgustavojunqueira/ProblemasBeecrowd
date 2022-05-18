n = int(input())
teste = 1

while n != 0:

    j1 = input()
    j2 = input()

    print(f"Teste {teste}")

    for i in range(n):
        a, b = map(int, input().split())

        if (a+b) % 2 == 0:
            print(j1)
        else:
            print(j2)

    n = int(input())
    teste += 1

    print()