#include <stdio.h>
#include <string.h>

int main(){

    char n[110], res[101];
    int d, digito, i, j, k;

    while(scanf("%i %s", &d, n) && d != '0' && strcmp(n, "0") != 0){

        for (i = 0, j = 0; i < strlen(n); i++) {
            
            digito = n[i] - '0';
            
            if (d != digito)
                res[j++] = n[i];
                
        }
        
        for (i = 0; i < j; i++)
            if (res[i] != '0')
                break;
        
        if (j == i)
            printf("0\n");
        else {
            for (k = i; k < j; k++)
                printf("%c", res[k]);
            
            printf("\n");
        }

    }

    return 0;
}