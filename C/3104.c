// Não funciona no beecrowd, acredito que seja por causa do tamanho do número

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int mod(char *numero, int divisor);

int main(){

    int divisor, res = 0;
    char *numero;

    numero = (char *) malloc( 1000 * sizeof(char));

    scanf("%s %i", numero, &divisor);

    res = mod(numero, divisor);

    free(numero);
}

int mod(char *numero, int divisor){
    int res;

    for (int i = 0, n = strlen(numero); i < n; i++){
        res = (res * 10 + (int)numero[i] - '0') % divisor;
    }

    printf("%i\n", res);
    return res;
}