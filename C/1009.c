#include <stdio.h>

int main(){

    char nome[15];
    double salario, valorVendas, total;

    scanf("%s", nome);
    scanf("%lf", &salario);
    scanf("%lf", &valorVendas);  

    total = salario + (valorVendas * 0.15);

    printf("TOTAL = R$ %.2lf\n", total);

    return 0;
}