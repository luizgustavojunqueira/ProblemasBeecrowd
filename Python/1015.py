x1, y1 = input().split(" ")
x2, y2 = input().split(" ")

x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)

dist = ( ( (x2-x1) ** 2) + ( (y2-y1) ** 2) ) ** (1/2)

print("{:.4f}".format(dist))
