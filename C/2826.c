#include <stdio.h>
#include <string.h>

int main(){

    char p1[20], p2[20];

    scanf("%s", p1);
    scanf("%s", p2);

    if(strcmp(p1, p2) > 0){
        printf("%s\n%s\n", p2, p1);
    }else{
        printf("%s\n%s\n", p1, p2);
    }

    return 0;
}