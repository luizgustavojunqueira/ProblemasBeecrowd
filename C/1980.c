#include <stdio.h>
#include <string.h>

int main(){

    char palavra[20];
    unsigned long long fatorial = 1;
    int tamanho = 0;

    while(1){

        scanf("%s", palavra);

        if(palavra[0] == '0'){
            break;
        }

        tamanho = (strlen(palavra));

        while(tamanho){
            fatorial *= tamanho--;
        }

        printf("%llu\n", fatorial);
        fatorial = 1;
    }

    return 0;
}