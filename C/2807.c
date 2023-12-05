#include <stdio.h>

int main(){

    int n, sequencia[40], anterior = 0, atual = 1, proximo = 0;

    scanf("%i", &n);

    for(int i = 0; i<n; i++){
        sequencia[i] = atual;
        proximo = atual + anterior;
        anterior = atual;
        atual = proximo;
    }

    for(int i = n-1; i > -1; i--){
        if(i == 0){
            printf("%i\n", sequencia[i]);
        }else{
            printf("%i ", sequencia[i]);
        }
    }

    return 0;
}