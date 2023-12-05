#include <stdio.h>
#include <stdlib.h>

int main(){

    char a[3], b[3];

    scanf("%s %s", a, b);

    int li, lf, ni, nf;

    li = (int) a[0];
    ni = (int) a[1];
    lf = (int) b[0];
    nf = (int) b[1];

    if((abs(lf-li) == 1 && abs(nf - ni) == 2) || (abs(lf-li) == 2 && abs(nf - ni) == 1)){
        printf("VALIDO\n");
    }else{
        printf("INVALIDO\n");
    }

    return 0;
}