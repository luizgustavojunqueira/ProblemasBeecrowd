n = int(input())

def segundoTermo(n):
    if n == 0:
        return 6
    else:
        x = 6 + 1 / segundoTermo(n-1)
        return x

res = segundoTermo(n) - 3

print(f"{res:.10f}")

# 1/(6+1/ (6+1/ (6+1) ) )