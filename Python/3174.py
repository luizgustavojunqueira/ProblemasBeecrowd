n = int(input())

hBonecos = 0
hArquitetos = 0
hMusicos = 0
hDesenhistas = 0

for i in range(n):
    name, group, hours = input().split()
    hours = int(hours)

    if group == "bonecos":
        hBonecos += hours
    elif group == "arquitetos":
        hArquitetos += hours
    elif group == "musicos":
        hMusicos += hours
    elif group == "desenhistas":
        hDesenhistas += hours
    
totalGifts = int(hBonecos//8 + hArquitetos//4 + hMusicos//6 + hDesenhistas//12)

print(totalGifts)