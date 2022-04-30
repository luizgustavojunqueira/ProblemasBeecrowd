while True:
    try:
        n = int(input())

        m = []

        for i in range(n):
            m.append([])
            for j in range(n):

                if i == j == n // 2:
                    m[i].append(4)
                elif n//3 <= i <= n - n//3 - 1 and n//3 <= j <= n - n//3 - 1:
                    m[i].append(1)
                elif i == j:
                    m[i].append(2)
                elif j == n - i-1:
                    m[i].append(3)
                else:
                    m[i].append(0)

                print(m[i][j], end = "")
            print()
        print()

    except EOFError:
        break