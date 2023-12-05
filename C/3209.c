#include <stdio.h>

int main(){

    int n, numStrips, totalOutlets = 0, numOutlets;

    scanf("%i", &n);

    for(int i = 0; i < n; i++){
        totalOutlets = 0;
        scanf("%i", &numStrips);

        for(int j = 0; j < numStrips; j++){
            scanf("%i", &numOutlets);
            totalOutlets += numOutlets;
        }

        printf("%i\n", totalOutlets - numStrips + 1);

    }

    return 0;
}