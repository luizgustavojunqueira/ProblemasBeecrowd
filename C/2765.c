#include <stdio.h>
#include <string.h>

int main(){
    char frase[128];
    
    while(gets(frase))
    {
        for(int i = 0; i < strlen(frase); i++)
        {
            if(frase[i] == ','){
                printf("\n");
            }else{
                printf("%c", frase[i]); 
            } 
        }
        printf("\n");
    }
    return 0;
}