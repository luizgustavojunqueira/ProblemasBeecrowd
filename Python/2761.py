entrada = list(input().split())

a = int(entrada[0])
b = float(entrada[1])
c = entrada[2]
d = ' '.join(entrada[3:])

tudo = str(a) + str(b) + c + d

print(tudo)
print("%d\t%f\t%c\t%s" % (a, b, c, d))
print("%10d%10.6f%10c%10s" % (a, b, c, d))
