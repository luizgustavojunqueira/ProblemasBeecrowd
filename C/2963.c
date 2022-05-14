#include <stdio.h>

int main(){

    int n, votosCarlos = 0, maior = 0, v;

    scanf("%i %i", &n, &votosCarlos);

    maior = votosCarlos;

    for(int i = 1; i < n; i++){
        scanf("%i", &v);

        if(v > maior){
            maior = v;
        }
    }

    if(maior == votosCarlos){
        printf("S\n");
    }else{
        printf("N\n");
    }

}