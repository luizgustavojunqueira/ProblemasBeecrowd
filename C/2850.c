#include <stdio.h>
#include <string.h>

int main(){

    char leg[8];

    while( scanf("%[^\n]%*c", leg) != EOF){
        if(strcmp(leg, "direita") == 0){
            printf("frances\n");
        }else if(strcmp(leg, "esquerda") == 0){
            printf("ingles\n");
        }else if(strcmp(leg, "nenhuma") == 0){
            printf("portugues\n");
        }else{
            printf("caiu\n");
        }
    }
    
    return 0;
}