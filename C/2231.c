#include <stdio.h>

int main(){

    int n, m, teste = 1;

    scanf("%i %i", &n, &m);

    while(1){
        if(n == 0 && m == 0){
            break;
        }

        int temperaturas[n], medias[n-m+1], maior = -200, menor = 200;

        for(int i = 0; i < n; i++){
            scanf("%i", &temperaturas[i]);
        }

        for(int i = 0, b = n-m+1; i < b; i++){
            int media = 0;

            for(int j = i, c = i+m; j < c; j++){
                media += temperaturas[j];
            }

            media = media / m;
            medias[i] = media;
            
            if(media < menor){
                menor = media;
            }

            if(media > maior){
                maior = media;
            }
        }

        printf("Teste %i\n", teste);
        printf("%i %i\n", menor, maior);
        printf("\n");

        scanf("%i %i", &n, &m);
        teste++;
    }

    return 0;
}