l, d = map(int, input().split())
k, p = map(int, input().split())

total = l * k + (l//d) * p

print(total)