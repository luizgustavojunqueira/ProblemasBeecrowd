#include <stdio.h>

int main(){

    int seg, hr, min;

    scanf("%i", &seg);

    hr = seg / 3600;
    seg = seg % 3600;
    min = seg / 60;
    seg = seg % 60;

    printf("%i:%i:%i\n", hr, min, seg);

    return 0;
}