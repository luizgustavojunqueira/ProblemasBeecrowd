#include <stdio.h>

int main(){

    double a, b, c, aTri, aCir, aTra, aQua, aRet;

    scanf("%lf %lf %lf", &a, &b, &c);

    aTri = (a*c)/2;
    aCir = c * c * 3.14159;
    aTra = ((a+b) * c) / 2;
    aQua = b*b;
    aRet = a * b;

    printf("TRIANGULO: %.3lf\n", aTri);
    printf("CIRCULO: %.3lf\n", aCir);
    printf("TRAPEZIO: %.3lf\n", aTra);
    printf("QUADRADO: %.3lf\n", aQua);
    printf("RETANGULO: %.3lf\n", aRet);

    return 0;
}