#include <stdio.h>

int main(){

    int n, maior = 0, x;

    scanf("%i", &n);

    for(int i = 0; i < n; i++){
        scanf("%i", &x);

        if(x > maior){
            maior = x;
        }
    }

    printf("%i\n", maior + 1);

    return 0;
}