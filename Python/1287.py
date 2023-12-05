while True:
    try:

        n = input()

        res = ""
        erro = False

        for i in range(len(n)):
            if n[i].isnumeric():
                res += n[i]
            elif n[i].lower() == "o":
                res += "0"
            elif n[i] == "l":
                res += "1"
            else:
                asc = ord(n[i].upper())
                if asc >= 65 and asc <= 90:
                    erro = True
                    break

        if erro == False and len(res) > 0:
            res = int(res)

            if res > 2147483647:
                print("error")
            else:
                print(res)
        else:
            print("error")

    except EOFError:
        break