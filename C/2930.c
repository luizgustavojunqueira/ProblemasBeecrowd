#include <stdio.h>

int main(){

    int e, d;

    scanf("%i %i", &e, &d);

    if(e > d){
        printf("Eu odeio a professora!\n");
    }else if(d-e >= 3){
        printf("Muito bem! Apresenta antes do Natal!\n");
    }else{
        printf("Parece o trabalho do meu filho!\n");
        if( e + 2 < 24){
            printf("TCC Apresentado!\n");
        }else{
            printf("Fail! Entao eh nataaaaal!\n");
        }
    }

    return 0;
}