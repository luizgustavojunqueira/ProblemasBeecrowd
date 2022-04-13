val = int(input())
v = []

for i in range(10):
    if i == 0:
        v.append(val)
    else:
        v.append(v[i-1] * 2)

for i in range(10):
    print(f"N[{i}] = {v[i]}")