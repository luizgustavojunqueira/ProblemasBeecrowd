while True:
    try:

        num = input()
        cpf = num[0] + num[1] + num[2] + "." + num[3] + num[4] + num[5] + "." + num[6] + num[7] + num[8] + "-" 

        b1 = 0

        for i in range(len(num)):
            b1 += (int(num[i]) * (i+1))

        b1 = b1%11
        if b1 == 10:
            b1 = 0

        b2 = 0

        multi = 9
        for i in range(len(num)):
            b2 += (int(num[i]) * multi)
            multi -= 1

        b2 = b2%11
        if b2 == 10:
            b2 = 0

        cpf += str(b1) + str(b2)

        print(cpf)

    except EOFError:
        break