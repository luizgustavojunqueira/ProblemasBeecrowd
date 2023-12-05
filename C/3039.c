#include <stdio.h>

int main(){

    int n, nCarrinhos = 0, nBonecas = 0;
    char nome[30], sexo;

    scanf("%i", &n);

    for(int i = 0; i < n; i++){
        scanf("%s %c", nome, &sexo);

        if(sexo == 'M'){
            nCarrinhos++;
        }else{
            nBonecas++;
        }
    }

    printf("%i carrinhos\n", nCarrinhos);
    printf("%i bonecas\n", nBonecas);

    return 0;
}