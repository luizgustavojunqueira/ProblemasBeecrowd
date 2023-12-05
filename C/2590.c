#include <stdio.h>

int main(){

    int ultimosDigitos[] = {1, 7, 9, 3}, t, n;

    scanf("%i", &t);

    for (int i = 0; i < t; i ++){
        scanf("%i", &n);

        printf("%i\n", ultimosDigitos[n%4]);
    }

    return 0;
}