notas = [float(i) for i in input().split()]

notas.remove(max(notas))
notas.remove(min(notas))

media = sum(notas) 
print(f"{media:.1f}")