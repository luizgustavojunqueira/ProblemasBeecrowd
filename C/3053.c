#include <stdio.h>
#include <string.h>

int main(){

    int n, copos[] = {0, 0, 0}, mov, aux, indexCopoFinal = 0;
    char copoInicio;

    scanf("%d %c", &n, &copoInicio);

    if(copoInicio == 'A'){
        copos[0] = 1;
    }else if(copoInicio == 'B'){
        copos[1] = 1;
    }else{
        copos[2] = 1;
    }

    for(int i = 0; i<n; i++){
        scanf("%i", &mov);

        if(mov == 1){
            aux = copos[0];
            copos[0] = copos[1];
            copos[1] = aux;
        }else if(mov == 2){
            aux = copos[1];
            copos[1] = copos[2];
            copos[2] = aux;
        }else{
            aux = copos[0];
            copos[0] = copos[2];
            copos[2] = aux;            
        }
    }

    for(int i = 0; i<3; i++){
        if (copos[i] == 1){
            indexCopoFinal = i;
        }
    }

    if(indexCopoFinal == 0){
        printf("A\n");
    }else if(indexCopoFinal == 1){
        printf("B\n");
    }else{
        printf("C\n");
    }

    return 0;
}