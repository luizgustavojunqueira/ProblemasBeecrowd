ret1X0, ret1Y0, ret1X1, ret1Y1 = map(int, input().split())
ret2X0, ret2Y0, ret2X1, ret2Y1 = map(int, input().split())

if (ret1X0 <= ret2X0 and ret2X0 <= ret1X1) and (ret1Y0 >= ret2Y0 and ret2Y0 >= ret1Y1):
    print(1)
elif (ret2X0 <= ret1X0 and ret1X0 <= ret2X1) and (ret2Y0 >= ret1Y0 and ret1Y0 >= ret2Y1):
    print(1)
else:
    print(0)
    