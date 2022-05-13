#include <stdio.h>

int main(){

    int n, a = 0, e = 0, h = 0, m = 0, x = 0;
    char nome[30], race;

    scanf("%i", &n);

    for(int i = 0; i < n; i++){
        scanf("%s %c", nome, &race);

        if(race == 'A'){
            a++;
        }else if(race == 'E'){
            e++;
        }else if(race == 'H'){
            h++;
        }else if(race == 'M'){
            m++;
        }else{
            x++;
        }
    }

    printf("%i Hobbit(s)\n", x);
    printf("%i Humano(s)\n", h);
    printf("%i Elfo(s)\n", e);
    printf("%i Anao(s)\n", a);
    printf("%i Mago(s)\n", m);

    return 0;
}