#include <stdio.h>

int main(){

    int c, x;

    scanf("%i", &c);

    for(int i = 0; i < c; i++){
        scanf("%i", &x);

        if(x > 8000){
            printf("Mais de 8000!\n");
        }else{
            printf("Inseto!\n");
        }
    }

    return 0;
}