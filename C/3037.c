#include <stdio.h>

int main(){

    int n, pJoao = 0, pMaria = 0, x, d;

    scanf("%i", &n);

    for(int i = 0; i< n; i++){
        for(int j = 0; j < 3; j++){
            scanf("%i %i", &x, &d);
            pJoao += x*d;
        }
        for(int j = 0; j < 3; j++){
            scanf("%i %i", &x, &d);
            pMaria += x*d;
        }

        if(pMaria > pJoao){
            printf("MARIA\n");
        }else{
            printf("JOAO\n");
        }
        
        pMaria = 0;
        pJoao = 0;
    }

    return 0;
}