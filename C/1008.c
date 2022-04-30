#include <stdio.h>

int main()
{
    
    int num, hrs;
    double valorHr, salario;

    scanf("%d", &num);
    scanf("%d", &hrs);
    scanf("%lf", &valorHr);
    
    salario = hrs * valorHr;

    printf("NUMBER = %i\n", num);
    printf("SALARY = U$ %.2lf\n", salario);

    return 0;
}
