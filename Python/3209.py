n = int(input())

for i in range(n):
    numStrips, numOutlets = input().split(" ", 1)
    numOutlets = list(map(int, numOutlets.split()))

    numAppliances = sum(numOutlets) - int(numStrips) + 1

    print(numAppliances)