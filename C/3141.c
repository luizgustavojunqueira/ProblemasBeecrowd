#include <stdio.h>

int main(){

    char nome[51];
    int dia, mes, ano, diaNasc, mesNasc, anoNasc;

    scanf("%[^\n]s", nome);
    scanf("%d/%d/%d", &dia, &mes, &ano);
    scanf("%d/%d/%d", &diaNasc, &mesNasc, &anoNasc);

    if(dia == diaNasc && mes == mesNasc){
        printf("Feliz aniversario!\n");
    }

    int d = (mes-mesNasc) * 31 + dia - diaNasc;

    if (d >= 0){
        printf("Voce tem %d anos %s.\n", (ano - anoNasc), nome);
    }else{
        printf("Voce tem %d anos %s.\n", (ano - anoNasc - 1), nome);
    }

    return 0;
}