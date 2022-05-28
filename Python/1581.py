n = int(input())

for i in range(n):
    k = int(input())

    diff = False
    lingua = input()
    for j in range(k-1):
        linguaNova = input()

        if linguaNova != lingua:
            lingua = "ingles"
            diff = True

        if not diff:
            lingua = linguaNova

    print(lingua)
