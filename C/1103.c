#include <stdio.h>

int main(){

    int h1, m1, h2, m2, diffHoras = 0, diffMin = 0;

    while(1){
        scanf("%i %i %i %i", &h1, &m1, &h2, &m2);

        if(h1 == 0 && h2 == 0 && m1 == 0 && m2 == 0){
            break;
        }else{

            diffHoras = h2 - h1;
            diffMin = m2 - m1;

            if (diffMin <= 0){
                diffHoras -= 1;
                diffMin += 60;
            }

            if(diffHoras < 0){
                diffHoras += 24;
            }

            printf("%i\n", (diffHoras * 60 + diffMin));

        }
    }

    return 0;
}