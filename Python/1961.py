altPulo, numCanos = map(int, input().split())
canos = input().split()

ganhou = True
for i in range(numCanos):
    canos[i] = int(canos[i])

for i in range(numCanos-1):
    if canos[i+1] - canos[i] > altPulo or canos[i] - canos[i+1] > altPulo:
        ganhou = False
    
if ganhou:
    print("YOU WIN")
else: 
    print("GAME OVER")