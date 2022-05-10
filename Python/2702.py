ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

res = 0

if cr > ca:
    res += cr - ca
if br > ba:
    res += br - ba
if pr > pa:
    res += pr - pa

print(res)