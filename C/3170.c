#include <stdio.h>
 
int main() {
 
    int b, g, falta;
    
    scanf("%i", &b);
    scanf("%i", &g);
    
    falta = (g/2) - b;
    
    if(falta > 0){
        printf("Faltam %i bolinha(s)\n", falta);
    }else{
        printf("Amelia tem todas bolinhas!\n");
    }
 
    return 0;
}