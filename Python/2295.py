a, g, ra, rg = map(float, input().split())

razaoRendimento = ra / rg
razaoPreco = a / g

if razaoPreco < razaoRendimento:
    print("A")
else:
    print("G")