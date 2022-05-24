#include <stdio.h>

int indexOf(int val);

int valoresCartas[] = {4, 5, 6, 7, 12, 11, 13, 1, 2, 3};

int main(){

    int n, adalberto = 0, bernadete = 0;

    scanf("%i", &n);

    for(int i = 0; i < n; i++){

        int a1, a2, a3, b1, b2, b3, rodadasA = 0, rodadasB = 0;

        scanf("%i %i %i %i %i %i", &a1, &a2, &a3, &b1, &b2, &b3);

        if(indexOf(a1) < indexOf(b1)){
            rodadasB += 1;
        }else{
            rodadasA += 1;
        }

        if(indexOf(a2) < indexOf(b2)){
            rodadasB += 1;
        }else{
            rodadasA += 1;
        }

        if(indexOf(a3) < indexOf(b3)){
            rodadasB += 1;
        }else{
            rodadasA += 1;
        }

        if(rodadasA >= rodadasB){
            adalberto += 1;
        }else{
            bernadete += 1;
        }
    }

    printf("%i %i\n", adalberto, bernadete);

    return 0;
}

int indexOf(int val){
    for (int i = 0; i < 10; i++){
        if (valoresCartas[i] == val){
            return i;
        }
    }
    return -1;
}