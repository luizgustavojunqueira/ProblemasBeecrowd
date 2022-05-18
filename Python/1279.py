anos = []

while True:
    try:

        anos.append(int(input()))

    except EOFError:
        break


for i in range(len(anos)):

    ano = anos[i]

    isLeap = False
    isHuluculu = False

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        isLeap = True
        print("This is leap year.")

    if ano % 15 == 0:
        isHuluculu = True
        print("This is huluculu festival year.")

    if ano % 55 == 0 and isLeap:
        print("This is bulukulu festival year.")

    if isLeap == False and isHuluculu == False:
        print("This is an ordinary year.")

    if i < len(anos) - 1:
        print()