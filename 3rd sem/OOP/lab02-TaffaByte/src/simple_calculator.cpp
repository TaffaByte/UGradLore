#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int num1;
    int num2;
    char op;
    cout << "Enter first number: " << endl;
    cin >> num1;
    cout << "Enter second number: " << endl;
    cin >> num2;
    cout << "Enter operation: " << endl;
    cin >> op;
    int num;
    switch (op) {

        case '+':
        num = num1 + num2;
        cout << num1 << " + " << num2 << " = " << num<< endl;
        break;

        case '-':
        num = num1 - num2;
        cout << num1 << " - " << num2 << " = " << num << endl;
        break;

        case '*':
        num = num1 * num2;
        cout << num1 << " * " << num2 << " = " << num<< endl;
        break;

        case '/':
        num = num1 / num2;
        cout << num1 << " / " << num2 << " = " << num << endl;
        break;

        case '^':
        num = pow(num1,num2);
        cout << num1 << " ^ " << num2 << " = " << num << endl;
        break;
    }
    return 0;

}