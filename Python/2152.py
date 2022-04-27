n = int(input())

for i in range(n):
    h, m, o = input().split()

    if len(h) == 1:
        h = f"0{h}"
    if len(m) == 1:
        m = f"0{m}"

    if o == "1":
        print(f"{h}:{m} - A porta abriu!")
    else:
        print(f"{h}:{m} - A porta fechou!")