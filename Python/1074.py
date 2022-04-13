n = int(input())
for i in range(0, n):
    x = int(input())

    msg = ""

    if x % 2 == 0:
        msg += "EVEN"
    else:
        msg += "ODD"
    if x > 0:
        msg += " POSITIVE"
    elif x < 0:
        msg += " NEGATIVE"
    else:
        msg = "NULL"
    print(msg)