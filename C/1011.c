#include <stdio.h>

int main(){

    int r;

    scanf("%d", &r);

    double volume = (4.0/3) * 3.14159 * r * r * r;

    printf("VOLUME = %.3lf\n", volume);

    return 0;
}