n = int(input())

edf = 0

for i in range(n):
    c, p = map(int, input().split())
    edf += c/p

if edf <= 1:
    print("OK")
else:
    print("FAIL")