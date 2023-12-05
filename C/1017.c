#include <stdio.h>

int main(){

    int t, v;
    double res;

    scanf("%i", &t);
    scanf("%i", &v);

    res = (v*t) / 12.0;

    printf("%.3lf\n", res);

    return 0;
}