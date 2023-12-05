t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    res = n
    
    if n >= k:
        res = n // k + n % k
    
    print(res)