#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){

    char s[20];

    while(scanf("%s", s) != EOF){
        unsigned long long soma = 0UL;

        for(int i = strlen(s) - 1, j = 0; i >= 0; i--, j++){
            soma += (s[i] - 'A' + 1) * (unsigned long long)pow(26,j);
        }

        if (soma <= 16384){
            printf("%llu\n", soma);
        }else{
            puts("Essa coluna nao existe Tobias!");
        }
    }

    return 0;
}