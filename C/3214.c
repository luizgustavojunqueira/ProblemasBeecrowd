#include <stdio.h>

int main(){

    int e, f, c, totalSodas = 0, totalEmpty = 0;

    scanf("%i %i %i", &e, &f, &c);

    totalEmpty = e + f;

    while (totalEmpty >= c){
        totalSodas++;
        totalEmpty += 1-c;  
    }
    
    printf("%i\n", totalSodas);

    return 0;
}