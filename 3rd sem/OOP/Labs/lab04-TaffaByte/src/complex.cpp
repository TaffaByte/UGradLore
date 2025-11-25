#include <iostream>
using namespace std;

void show(double *complex) {
    cout << complex[0];
    if (complex[1] >= 0)
        cout << " + " << complex[1] << "i";
    else
        cout << " - " << -complex[1] << "i";
    cout << endl;
}

void add(double *c1, double *c2, double *result) {
    result[0] = c1[0] + c2[0];
    result[1] = c1[1] + c2[1];
}
void add(double *c1, double realNum, double *result) {
    result[0] = c1[0] + realNum;
    result[1] = c1[1];
}

void subtract(double *c1, double *c2, double *result) {
    result[0] = c1[0] - c2[0];
    result[1] = c1[1] - c2[1];
}
void subtract(double *c1, double realNum, double *result) {
    result[0] = c1[0] - realNum;
    result[1] = c1[1];
}

void multiply(double *c1, double *c2, double *result) {
    result[0] = c1[0] * c2[0] - c1[1] * c2[1];  
    result[1] = c1[0] * c2[1] + c1[1] * c2[0];
}
void multiply(double *c1, double realNum, double *result) {
    result[0] = c1[0] * realNum;
    result[1] = c1[1] * realNum;
}

int main() {
    double c1[2], c2[2], res[2];
    double d1;

    cout << "Enter c1: ";
    cin >> c1[0] >> c1[1];
    cout << "Enter c2: ";
    cin >> c2[0] >> c2[1];
    cout << "Enter d1: ";
    cin >> d1;

    cout << "c1: "; show(c1);
    cout << "c2: "; show(c2);

    add(c1, c2, res);
    cout << "c1+c2: "; show(res);

    subtract(c1, c2, res);
    cout << "c1-c2: "; show(res);

    multiply(c1, c2, res);
    cout << "c1*c2: "; show(res);

    add(c1, d1, res);
    cout << "c1+d1: "; show(res);

    subtract(c1, d1, res);
    cout << "c1-d1: "; show(res);

    multiply(c1, d1, res);
    cout << "c1*d1: "; show(res);

    return 0;
}

