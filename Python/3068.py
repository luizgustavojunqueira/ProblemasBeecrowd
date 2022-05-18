x1, y1, x2, y2 = map(int, input().split())

teste = 1

while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:

    qntMeteoritos = 0

    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())

        if (x1 <= x and x <= x2) and (y1 >= y and y >= y2):
            qntMeteoritos += 1

    print(f"Teste {teste}")
    print(qntMeteoritos)
    
    teste += 1
    x1, y1, x2, y2 = map(int, input().split())