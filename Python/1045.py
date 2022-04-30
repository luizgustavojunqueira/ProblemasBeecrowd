a,b,c = map(float, input().split())

aux = 0

if b > a and b > c:
    aux = a
    a = b
    b = aux
elif c > a and c > b:
    aux = a
    a = c
    c = aux

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    elif a ** 2 > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif a ** 2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
        
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b!= a):
        print("TRIANGULO ISOSCELES")