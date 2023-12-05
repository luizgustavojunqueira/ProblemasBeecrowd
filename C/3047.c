#include <stdio.h>
#include <stdlib.h>

int main(){

    int m, a, b, c = 0, maior;

    scanf("%i %i %i", &m, &a, &b);

    c = m - (a+b);

    maior = (a+b + abs(a-b)) / 2;
    maior = (maior + c + abs(maior - c)) / 2;

    printf("%i\n", maior);

    return 0;
}