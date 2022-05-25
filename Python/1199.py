n = input()

while n != "-1":

    if n[:2] == "0x":
        print(str(int(n, 16)))
    else:
        x = str(hex(int(n)))[2:].upper()
        print(f"0x{x}")

    n = input()