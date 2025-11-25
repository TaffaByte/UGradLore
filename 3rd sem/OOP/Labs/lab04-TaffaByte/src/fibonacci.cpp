#include <iostream>
using namespace std;

long fib(int n) {
    if (n == 0 || n == 1)
        return 1;
    return fib(n - 1) + fib(n - 2);
}

long fib(int n, bool count) {
    static long calls = 0;
    calls++;

    if (n == 0 || n == 1)
        return 1;

    long result = fib(n - 1, count) + fib(n - 2, count);

    if (n == 1)
        cout << "Function was called " << calls << " times.\n";

    return result;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    cout << "fib(" << n << ") = " << fib(n) << endl;
    cout << "Now with counting calls:\n";
    cout << "fib(" << n << ") = " << fib(n, true) << endl;

    return 0;
}
