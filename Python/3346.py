f1, f2 = map(float, input().split())

res = (100 + f1) * (f2/100 + 1) - 100

print(f"{res:.6f}")