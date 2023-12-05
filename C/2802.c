#include <stdio.h>

int main(){

    long long n, resposta;

    scanf("%lli", &n);

    resposta = 1 + (n* (n-1)) / 2 + (n * (n-1) * (n-2) * (n-3)) / 24;

    printf("%lld\n", resposta);

    return 0;
}