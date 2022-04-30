antigo, novo = map(float, input().split())

percent = ((novo / antigo) - 1) * 100

print(f"{percent:.2f}%")