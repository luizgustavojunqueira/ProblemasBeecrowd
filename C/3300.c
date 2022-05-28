#include <stdio.h>
#include <string.h>

int main(){

    char num[101];

    scanf("%s", num);

    if(strstr(num, "13") != NULL){
        printf("%s es de Mala Suerte\n", num);
    }else{
        printf("%s NO es de Mala Suerte\n", num);
    }

    return 0;
}