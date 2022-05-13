#include <stdio.h>

int main(){

    int n, c, p;
    double edf = 0;

    scanf("%i", &n);

    for(int i = 0; i < n; i++){
        scanf("%i %i", &c, &p);

        edf += (double) c / p;
    }

    if(edf <= 1){
        printf("OK\n");
    }else{
        printf("FAIL\n");
    }

    return 0;
}