#include <iostream>

using namespace std;

int abs(int x){
  if(x < 0){
    return -x;
  }
  return x;
}

int main() {

  int m = 0;

  cin >> m;

  while (m > 0){
    int posAtual = 2;
    int numToques = 0;
    int esq = 0, cen = 0, dir = 0;

    for(int i = 0; i < m; i++){
      cin >> esq >> cen >> dir;
      
      if(esq == 0 && cen == 1 && dir == 1 && posAtual != 1){
        numToques = numToques + abs(posAtual - 1);
        posAtual = 1;
      } else if(esq == 1 && cen == 0 && dir == 1 && posAtual != 2){
        numToques = numToques + abs(posAtual - 2);
        posAtual = 2;
      } else if(esq == 1 && cen == 1 && dir == 0 && posAtual != 3){
        numToques = numToques + abs(posAtual - 3);
        posAtual = 3;
      } 
    }

    cout << numToques << endl;
    cin >> m;
  }

  return 0;
}
