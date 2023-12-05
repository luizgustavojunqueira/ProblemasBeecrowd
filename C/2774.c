#include <stdio.h>
#include <math.h>

int main(){

    int h, m, numTestes;

    while(scanf("%i %i", &h, &m) != EOF){
        numTestes = (h*60) / m;

        double valores[numTestes], media = 0, precisao = 0;

        for(int i=0; i<numTestes; i++){
            scanf("%lf", &valores[i]);
            media += valores[i];
        }

        media = media / (float) numTestes;

        for (int i = 0; i < numTestes; i++){
            precisao += pow((valores[i] - media), 2);
        }

        precisao = precisao / (numTestes - 1);
        precisao = sqrt(precisao);

        printf("%.5lf\n", precisao);
    }

    return 0;
}