#include <stdio.h>

int main(){

    int t, pa, pb, anos = 0;
    double g1, g2;

    scanf("%i", &t);

    for(int i = 0; i < t; i++){

        scanf("%i %i %lf %lf", &pa, &pb, &g1, &g2);

        while(pa <= pb){
            pa += pa * (g1/100);
            pb += pb * (g2/100);
            anos += 1;

            if(anos > 100){
                printf("Mais de 1 seculo.\n");
                break;
            }
        }

        if(anos <= 100){
            printf("%i anos.\n", anos);
        }
        

        anos = 0;
    }

    return 0;
}