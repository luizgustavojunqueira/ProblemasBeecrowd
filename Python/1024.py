n = int(input())

for i in range(n):
    msg = [c for c in input()]

    t = int(len(msg) / 2)

    for j in range(len(msg)):
        if not msg[j].isnumeric() and msg[j] != " " and msg[j].isalpha():
            msg[j] = chr(ord(msg[j]) + 3)

    msg = msg[::-1]

    for j in range(t, len(msg)):
        msg[j] = chr(ord(msg[j]) - 1)

    print("".join(msg))