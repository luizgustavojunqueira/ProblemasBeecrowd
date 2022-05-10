k = int(input())       

while k != 0:

    n, m = map(int, input().split())
    for i in range(k):

        x, y = map(int, input().split())

        if x == n or y == m:
            print("divisa")
        elif x > n and y > m:
            print("NE")
        elif x < n and y > m:
            print("NO")
        elif x < n and y < m:
            print("SO")
        elif x > n and y < m:
            print("SE")
    k = int(input())    