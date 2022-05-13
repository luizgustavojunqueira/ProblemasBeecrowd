n = int(input())

a,e,h,m,x = 0, 0, 0, 0, 0

for i in range(n):
    name, race = input().split()
    
    if race == "A":
        a += 1
    elif race == "E":
        e += 1
    elif race == "H":
        h += 1
    elif race == "M":
        m += 1
    else:
        x += 1

print(f"{x} Hobbit(s)")
print(f"{h} Humano(s)")
print(f"{e} Elfo(s)")
print(f"{a} Anao(s)")
print(f"{m} Mago(s)")