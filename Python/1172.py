v = []

for i in range(10):
    v.append(int(input()))

for i in range(10):
    if v[i] <= 0:
        v[i] = 1

for i in range(10):
    print(f"X[{i}] = {v[i]}")