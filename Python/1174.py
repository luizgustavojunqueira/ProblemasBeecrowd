v = []

for i in range(100):
    v.append(float(input()))

for i in range(100):
    if v[i] <= 10:
        print(f"A[{i}] = {v[i]}")