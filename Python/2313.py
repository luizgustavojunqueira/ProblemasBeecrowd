a, b, c = map(int, input().split())

if a > b-c and b > a-c and c > b-a:
    tipoTriangulo = ""

    if a == b != c or a == c != b or b == c != a:
        tipoTriangulo = "Isoceles"
    elif a == b == c:
        tipoTriangulo = "Equilatero"
    else:
        tipoTriangulo = "Escaleno"

    retangulo = "N"

    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
        retangulo = "S"

    print(f"Valido-{tipoTriangulo}")
    print(f"Retangulo: {retangulo}")

else:
    print("Invalido")