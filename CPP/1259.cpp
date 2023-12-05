#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void bubbleSort(int n, int v[]);

int main(){

    int n, x, qntPares = 0, qntImpares = 0;

    cin >> n;
    int pares[n], impares[n];

    for(int i = 0; i < n; i++){
        cin >> x;
        if(x % 2 == 0){
            pares[qntPares] = x;
            qntPares++;
        }else{
            impares[qntImpares] = x;
            qntImpares++;
        }
    }

    vector<int> vectorPares (pares, pares+qntPares);
    vector<int> vectorImpares (impares, impares+qntImpares);

    sort(vectorPares.begin(), vectorPares.end());
    sort(vectorImpares.begin(), vectorImpares.end());

    for(int i = 0; i < qntPares; i++){
        cout << vectorPares[i] << endl;
    }

    for(int i = qntImpares - 1; i >= 0; i--){
        cout << vectorImpares[i] << endl;
    }

}

void troca(int &a, int &b){
    int aux = a;
    a = b;
    b = aux;
}

void bubbleSort(int n, int v[]){
    for(int i = n-1; i > 0; i--){
        for(int j = 0; j < i; j++){
            if(v[j] > v[j+1]){
                troca(v[j], v[j+1]);
            }
        }
    }
}