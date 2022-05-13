#include <stdio.h>

int fibonot(int k);

int main(){

    int k;

    scanf("%i", &k);

    printf("%i\n", fibonot(k));

    return 0;
}

int fibonot(int k){
    int anterior = 1, atual = 2, proximo = 3;

    while(k > 0){
        anterior = atual;
        atual = proximo;
        proximo = anterior + atual;

        k -= (anterior - 1);
    }

    k += (anterior - 1);

    return atual + k;
}