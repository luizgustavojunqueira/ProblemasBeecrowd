n = int(input())

for i in range(n):
    b = int(input())
    atkD, defD, lvlD = map(int, input().split())
    atkG, defG, lvlG = map(int, input().split())

    golpeD = (atkD + defD) / 2
    golpeG = (atkG + defG) / 2

    if lvlD % 2 == 0:
        golpeD += b
    if lvlG % 2 == 0:
        golpeG += b

    if golpeG > golpeD:
        print("Guarte")
    elif golpeG < golpeD:
        print("Dabriel")
    else:
        print("Empate")