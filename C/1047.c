#include <stdio.h>

int main(){

    int hi, mi, hf, mf, duracaoH, duracaoM, diff;

    scanf("%i %i %i %i", &hi, &mi, &hf, &mf);

    diff = (hf * 60 + mf) - (hi * 60 + mi); // Diferença de minutos

    if (diff <= 0){
        diff += 60 * 24;
    }

    duracaoH = diff / 60;
    duracaoM = diff % 60;

    printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n", duracaoH, duracaoM);
    
    return 0;
}