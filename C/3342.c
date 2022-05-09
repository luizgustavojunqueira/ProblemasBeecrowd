#include <stdio.h>

int main(){

    int n, nBrancas = 0, nPretas;
    scanf("%i", &n);

    n = n*n;

    nPretas = n/2;

    if (n%2==0){
        nBrancas = nPretas;
    }else{
        nBrancas = (n+1) / 2;
    }

    printf("%i casas brancas e %i casas pretas\n", nBrancas, nPretas);

    return 0;
}