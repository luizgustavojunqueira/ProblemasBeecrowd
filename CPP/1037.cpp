#include <iostream>

using namespace std;

int main(){

    double valor;

    cin >> valor;

    

    if(valor < 0 || valor > 100){
        cout << "Fora de intervalo" << endl;
    }else {
        cout << "Intervalo ";
        if(valor <= 25){
            cout << "[0,25]" << endl;
        }else if(valor <= 50){
            cout << "(25,50]" << endl;
        }else if(valor <= 75){
            cout << "(50,75]" << endl;
        }else if(valor <= 100){
            cout << "(75,100]" << endl;
        }
    }

    return 0;
}