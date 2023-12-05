#include <stdio.h>
#include <string.h>

int main(){

    int n, totalPresentes, hB =  0, hA = 0, hM = 0, hD = 0, horas;
    char nome[30], grupo[30];

    scanf("%d", &n);

    for (int i = 0; i < n; i++){
        scanf("%s %s %d", nome, grupo, &horas);

        if(strcmp(grupo, "bonecos") == 0){
            hB += horas;
        }else if(strcmp(grupo, "arquitetos") == 0){
            hA += horas;
        }else if(strcmp(grupo, "musicos") == 0){
            hM += horas;
        }else if(strcmp(grupo, "desenhistas") == 0){
            hD += horas;
        }
    }

    totalPresentes = hB/8 + hA/4 + hM/6 + hD/12;

    printf("%i\n", totalPresentes);

    return 0;
}