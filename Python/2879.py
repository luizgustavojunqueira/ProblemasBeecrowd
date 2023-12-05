n = int(input())

vezesGanhadas = 0

for i in range(n):
    portaCerta = int(input())
    
    if portaCerta != 1:
        vezesGanhadas += 1

print(vezesGanhadas)