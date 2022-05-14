while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == m1 == h2 == m2 == 0:
        break
    else:

        diffHoras = h2 - h1

        diffMin = m2 - m1

        if diffMin <= 0:
            diffHoras -= 1
            diffMin += 60     

        if diffHoras < 0:
            diffHoras += 24
    
        print(diffHoras * 60 + diffMin)