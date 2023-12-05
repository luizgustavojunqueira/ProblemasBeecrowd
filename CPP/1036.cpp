#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){

    double a, b, c, delta, r1, r2;

    cin >> a >> b >> c;

    delta = (b * b) - (4*a*c);

    if(delta >= 0 && a > 0){
        delta = sqrt(delta);

        r1 = (-b + delta) / (2 * a);
        r2 = (-b - delta) / (2 * a);

        cout << "R1 = " << fixed << setprecision(5) << r1 << endl;
        cout << "R2 = " << fixed << setprecision(5) << r2 << endl;
    }else{
        cout << "Impossivel calcular" << endl;
    }

    return 0;
}