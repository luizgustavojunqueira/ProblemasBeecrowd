while True:
    try:

        num = input()
        num = num.replace(".","").replace("-","")
        b1 = int(num[-2])
        b2 = int(num[-1])
        num = num[:9]

        b1Real = 0

        for i in range(len(num)):
            b1Real += (int(num[i]) * (i+1))

        b1Real = b1Real%11
        if b1Real == 10:
            b1Real = 0

        b2Real = 0

        multi = 9
        for i in range(len(num)):
            b2Real += (int(num[i]) * multi)
            multi -= 1

        b2Real = b2Real%11
        if b2Real == 10:
            b2Real = 0

        if b2Real == b2 and b1Real == b1:
            print("CPF valido")
        else:
            print("CPF invalido")

    except EOFError:
        break