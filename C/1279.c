#include <stdio.h>

int main(){

    int ano;

    while(scanf("%i", &ano) != EOF){

        int isLeap = 0, isHuluculu = 0;

        if((ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0){
            isLeap = 1;
            printf("This is leap year.\n");
        } 

        if(ano % 15 == 0){
            isHuluculu = 1;
            printf("This is huluculu festival year.\n");
        }

        if(isLeap == 1 && ano % 55 == 0){
            printf("This is bulukulu festival year.\n");
        }

        if(isLeap == 0 && isHuluculu == 0){
            printf("This is an ordinary year.\n");
        }

        printf("\n");

    }

    return 0;
}