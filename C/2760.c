#include <stdio.h>
#include <string.h>
int main() {
    char frases[3][101];
    int i = 0, j = 3, ini;
    while (i < 3) {
        gets(frases[i]);
        i++;
    }
    for (j = 3, ini = 0; j < 6; j++, ini++) {
        for (i = ini; i < j; i++)
            printf("%s", frases[i%3]);
        printf("\n");
    }
    for (i = 0; i < 3; i++) {
        if (strlen(frases[i]) < 10)
            printf("%s", frases[i]);
        else {
            for (j = 0; j < 10; j++)
                printf("%c", frases[i][j]);
        }
    }
    printf("\n");
    return 0;
}