#include <stdio.h>
#include <string.h>
#include <ctype.h>

char vogais[] = "aeiou";

int ehConsoante(char c);

int main(){

    int n, facil = 1;
    char nome[43] = "", nomeLower[43] = "";

    scanf("%i", &n);

    for(int i = 0; i < n; i++){

        facil = 1;
        scanf("%s", nome);

        for(int j = 0, len = strlen(nome); j < len; j++){
            nomeLower[j] = tolower(nome[j]);
        }

        for(int j = 0, len = strlen(nome) - 2; j < len; j++){
            if(ehConsoante(nomeLower[j]) && ehConsoante(nomeLower[j+1]) && ehConsoante(nomeLower[j+2])){
                facil = 0;
            }
        }

        if(facil == 1){
            printf("%s eh facil\n", nome);
        }else if(facil == 0){
            printf("%s nao eh facil\n", nome);
        }

    }

    return 0;
}

int ehConsoante(char c){
    int e = 1;

    for(int i = 0; i < 5; i++){
        if(vogais[i] == c){
            e = 0;
        }
    }

    return e;
}