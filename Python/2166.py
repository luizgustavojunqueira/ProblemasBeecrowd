n = int(input())

def r2(n):
    if n == 0:
        return 2
    else:
        x = 2 + 1 / r2(n-1)
        return x

print(f"{r2(n) - 1:.10f}")