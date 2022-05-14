#include <stdio.h>
#include <math.h>

int main(){

    int v, n, totalSigns = 0;
    double signs = 0;

    scanf("%i %i", &v, &n);

    totalSigns = v * n;

    for(int i = 1; i < 10; i++){
        signs = (totalSigns * i) / 10.0;
        if(fmod(signs, 1) != 0){
            signs += 1;
        }

        if (i == 9){
            printf("%i\n", (int) signs);
        }else{
            printf("%i ", (int) signs);
        }
    }

    return 0;
}