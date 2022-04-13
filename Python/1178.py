x = float(input())

n = [x]

for i in range(1, 100):
    n.append(n[i-1] / 2)

for i in range(100):
    print(f"N[{i}] = {n[i]:.4f}")