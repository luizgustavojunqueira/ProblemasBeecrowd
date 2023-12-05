#include <stdio.h>

int main(){

    int valorReal, valorCents, nota100, nota50, nota20, nota10, nota5, nota2, moeda100, moeda50, moeda25, moeda10, moeda5, resto;

    scanf("%d.%d", &valorReal, &valorCents);


    nota100 = valorReal / 100;
    resto = valorReal % 100;

    nota50 = resto / 50;
    resto = resto % 50;

    nota20 = resto / 20;
    resto = resto % 20;

    nota10 = resto / 10;
    resto = resto % 10;

    nota5 = resto / 5;
    resto = resto % 5;

    nota2 = resto / 2;
    resto = resto % 2;

    resto = (resto*100) + valorCents;

    moeda100 = resto / 100;
    resto = resto % 100;

    moeda50 = resto / 50;
    resto = resto % 50;

    moeda25 = resto / 25;
    resto = resto % 25;

    moeda10 = resto / 10;
    resto = resto % 10;

    moeda5 = resto / 5;
    resto = resto % 5;

    printf("NOTAS:\n");
    printf("%i nota(s) de R$ 100.00\n", nota100);
    printf("%i nota(s) de R$ 50.00\n", nota50);
    printf("%i nota(s) de R$ 20.00\n", nota20);
    printf("%i nota(s) de R$ 10.00\n", nota10);
    printf("%i nota(s) de R$ 5.00\n", nota5);
    printf("%i nota(s) de R$ 2.00\n", nota2);
    printf("MOEDAS:\n");
    printf("%i moeda(s) de R$ 1.00\n", moeda100);
    printf("%i moeda(s) de R$ 0.50\n", moeda50);
    printf("%i moeda(s) de R$ 0.25\n", moeda25);
    printf("%i moeda(s) de R$ 0.10\n", moeda10);
    printf("%i moeda(s) de R$ 0.05\n", moeda5);
    printf("%i moeda(s) de R$ 0.01\n", resto);

    return 0;
}