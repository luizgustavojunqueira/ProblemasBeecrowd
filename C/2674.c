#include <stdio.h>
#include <math.h>

int ehPrimo(int n);

int main(){

    int n;

    while(scanf("%i", &n) != EOF){
        int primo = ehPrimo(n), super = 0;

        if(primo == 1){
            do {
                int digito = n % 10;
                super = ehPrimo(digito);
                if(super == 0){
                    break;
                }
            } while (n/=10);

            if(super == 1){
                printf("Super\n");
            }else{
                printf("Primo\n");
            }
        }else{
            printf("Nada\n");
        }
    }

    return 0;
}

int ehPrimo(int n){
    if (n <= 3){
        return n > 1;
    }

    if(n%2 == 0 || n%3 == 0){
        return 0;
    }

    int i = 5, stop = sqrt(n);

    while(i <= stop){
        if(n%i == 0 || n%(i+2) == 0){
            return 0;
        }
        i += 6;
    }

    return 1;

}