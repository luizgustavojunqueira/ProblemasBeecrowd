#include <stdio.h>
 
int main() {
    
    int h, e, a, o, w, x;
    
    scanf("%i %i %i %i %i %i", &h, &e, &a, &o, &w, &x);
    
    if(h + e + a + x >= w + o){
        printf("Middle-earth is safe.\n");   
    }else{
        printf("Sauron has returned.\n");
    }
 
    return 0;
}