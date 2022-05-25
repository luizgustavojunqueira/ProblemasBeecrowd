import struct

a, b, c, d = input().split(" ",maxsplit = 3)
b = float(b)
b = struct.unpack('f', struct.pack('f', b))[0]
a = int(a)
print(str(a)+"%.6f"%b+c+d)
print("%d\t%f\t%c\t%s" % (a, b, c, d))
print("%10d%10.6f%10c%10s" % (a, b, c, d))