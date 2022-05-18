import sys
sys.stdin.reconfigure(errors="ignore")

t = int(input())

for instancia in range(t):
    correto = input()
    time1 = input()
    time2 = input()

    contadorTime1 = 0
    contadorTime2 = 0
    errouTime1 = False
    errouTime2 = False
    posiErradoTime1 = 0
    posiErradoTIme2 = 0

    if len(time1) == len(correto) and len(time2) == len(correto):

        for i in range(len(correto)):
            if time1[i] == correto[i]:
                contadorTime1 += 1
            else:
                if not errouTime1:
                    posiErradoTime1 = i
                    errouTime1 = True
            
            if time2[i] == correto[i]:
                contadorTime2 += 1
            else:
                if not errouTime2:
                    posiErradoTime2 = i
                    errouTime2 = True

            if posiErradoTime1 == posiErradoTime2:
                errouTime1 = False
                errouTime2 = False

    print(f"Instancia {instancia+1}")

    if contadorTime1 == contadorTime2 and errouTime1 == True and errouTime2 == True and posiErradoTime1 > posiErradoTime2:
        print("time 1")
    elif contadorTime1 == contadorTime2 and errouTime1 == True and errouTime2 == True and posiErradoTime1 < posiErradoTime2:
        print("time 2")
    elif contadorTime1 == contadorTime2:
        print("empate")
    elif contadorTime1 > contadorTime2:
        print("time 1")
    else:
        print("time 2")

    print()