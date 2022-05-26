a = int(input())
b = int(input())
c = int(input())

print(f"A = {a}, B = {b}, C = {c}")
print(f"A = {a:10d}, B = {b:10d}, C = {c:10d}")
print(f"A = {a:010d}, B = {b:010d}, C = {c:010d}")
print(f"A = {str(a).ljust(10)}, B = {str(b).ljust(10)}, C = {str(c).ljust(10)}")