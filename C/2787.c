#include <stdio.h>

int main(){

    int l, c;

    scanf("%i", &l);
    scanf("%i", &c);

    if((l + c) % 2 == 0){
        printf("%d\n", 1);
    }else{
        printf("%d\n", 0);
    }

    return 0;
}