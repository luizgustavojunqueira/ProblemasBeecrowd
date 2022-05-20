#include <stdio.h>

int main(){

    int m, passoSomatoria;

    while(scanf("%i", &m) != EOF){

        int valoresMoedas[m], soma = 0, numDivisores = 0;

        for(int i = 0; i < m; i++){
            scanf("%i", &valoresMoedas[i]);
        }

        scanf("%i", &passoSomatoria);

        for (int i = m-1; i >= 0; i -= passoSomatoria){
            soma += valoresMoedas[i];
        }

        for(int i = 1, b = soma+1; i < b; i++ ){
            if(soma % i == 0){
                numDivisores += 1;
            } 
        }

        if(numDivisores == 2){
            printf("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");
        }else{
            printf("Bad boy! I’ll hit you.\n");
        }

    }

    return 0;
}