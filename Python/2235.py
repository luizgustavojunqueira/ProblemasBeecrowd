a, b, c = map(int, input().split())

if a - b == 0:
    print("S")
elif a - c == 0:
    print("S")
elif b - c == 0:
    print("S")
elif a + b - c == 0:
    print("S")
elif a - b + c == 0:
    print("S")
elif a - b - c == 0:
    print("S")
elif -a + b + c == 0:
    print("S")
elif-a + b - c == 0:
    print("S")
elif -a - b + c == 0:
    print("S")
elif -a - b - c == 0:
    print("S")
else:
    print("N")