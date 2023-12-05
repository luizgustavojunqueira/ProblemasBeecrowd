#include <stdio.h>
#include <string.h>

int ehSubSequencia(char *str1, char *str2);

int main(){

    int n, q;
    char s[100001], r[101];

    scanf("%i", &n);

    for(int i = 0; i < n; i++){

        scanf("%s", s);
        scanf("%i", &q);

        for(int j = 0; j < q; j++){

            scanf("%s", r);

            if(ehSubSequencia(r, s)){
                printf("Yes\n");
            }else{
                printf("No\n");
            }

        }

    }

    return 0;
}

int ehSubSequencia(char *str1, char *str2){
    int lenStr1 = strlen(str1), lenStr2 = strlen(str2), indexStr1 = 0, indexStr2 = 0;

    while(indexStr1 < lenStr1 && indexStr2 < lenStr2){
        if(str1[indexStr1] == str2[indexStr2]){
            indexStr1++;
        }
        indexStr2++;
    }

    return indexStr1 == lenStr1;
}