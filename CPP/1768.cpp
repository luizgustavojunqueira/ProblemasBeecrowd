#include <iostream>

using namespace std;

int main(){

    int n;

    while(cin>>n){

        int x = 1;

        while (x<=n){
            for(int i = 0; i < (n-x)/2; i++){
                cout << " ";
            }
            for(int i = 0; i < x; i++){
                cout << "*";
            }
            cout << endl;
            x += 2;
        }

        x = 1;

        while (x<=3){
            for(int i = 0; i < (n-x)/2; i++){
                cout << " ";
            }
            for(int i = 0; i < x; i++){
                cout << "*";
            }
            cout << endl;
            x += 2;
        }

        cout << endl;

    }

}