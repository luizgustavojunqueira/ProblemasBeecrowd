/*
    NÂO FUNCIONA AINDA
*/


#include <stdio.h>

int main(){

    int n, atual = 0, totalCarneiros = 0, carneirosRoubados = 0, numAnterior = 0, ultimaPos = 0, numRoubadas = 0;

    scanf("%d",&n);

    int numCarneiros[n], estrelasRoubadas[n];

    for(int i=0; i<n; i++)
    {
        scanf("%d", &numCarneiros[i]);
        totalCarneiros += numCarneiros[i];
        estrelasRoubadas[i] = 0;
    }

    while(1){

        if(numCarneiros[atual] > 0){

            numAnterior = numCarneiros[atual];

            carneirosRoubados += 1;
            numCarneiros[atual] -= 1;

            int roubada = 0;

            for(int i = 0; i < n; i++){
                if(estrelasRoubadas[i] == atual){
                    roubada = 1;
                }
            }

            if(roubada == 0){
                estrelasRoubadas[ultimaPos] = atual;
                ultimaPos += 1;
                numRoubadas += 1;
            }

            if((numAnterior % 2) == 0){
                atual -= 1;
            }else{
                atual += 1;
            }

        }else{
            break;
        }

        if(atual < 0 || atual >= n){
            break;
        }

    }

    printf("%i %i\n", numRoubadas+1, totalCarneiros - carneirosRoubados);

    return 0;
}