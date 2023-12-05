#include <stdio.h>
#include <string.h>

int main(){

    char jeepSituation[7];
    int t, tSalida = 0, tVuelta = 0, qntJeepSalida = 0, qntJeepVuelta = 0;

    scanf("%s", jeepSituation);

    while(strcmp(jeepSituation, "ABEND") != 0){
        scanf("%i", &t);

        if (strcmp(jeepSituation, "SALIDA") == 0){
            qntJeepSalida++;
            tSalida += t;
        }else{
            qntJeepVuelta++;
            tVuelta += t;
        }

        scanf("%s", jeepSituation);
    }

    printf("%i\n%i\n", (tSalida - tVuelta), (qntJeepSalida - qntJeepVuelta));

    return 0;
}