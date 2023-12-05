#include <stdio.h>

int main(){

    int ano, mes, dia;

    scanf("%i", &dia);

    ano = dia / 365;
    dia = dia % 365;
    mes = dia / 30;
    dia = dia % 30;

    printf("%i ano(s)\n", ano);
    printf("%i mes(es)\n", mes);
    printf("%i dia(s)\n", dia);

    return 0;
}