#include <stdio.h>
#include <stdlib.h>

int main(){

    int a, b, q, r;

    scanf("%i %i", &a, &b);

    if(a > 0){
        r = a % b;
        q = (a-r) / b;
    }else{
        for (int i = 0; i<= abs(b); i++){ // 0 <= r <= |b|
            if((a-i) % b == 0){ // Se a-r é divisivel por b, ent esse resultado é o q, pq a = b*q + r => q = (a-r) / b
                q = (a-i) / b;
                r = i;
                break;
            }
        }
    }

    printf("%i %i\n", q, r);

    return 0;
}