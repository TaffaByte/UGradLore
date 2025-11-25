#include <iostream>
#include <cstring>
using namespace std;

int holesInDigit(int digit) {
    switch (digit) {
        case 0: case 4: case 6: case 9: return 1;
        case 8: return 2;
        default: return 0;
    }
}

int holesInChar(char c) {
    switch (c) {
        case 'A': case 'D': case 'O': case 'P': case 'Q': case 'R': return 1;
        case 'B': return 2;
        default: return 0;
    }
}

int countHoles(int n) {
    if (n == 0) return 0;
    int lastDigit = n % 10;
    return holesInDigit(lastDigit) + countHoles(n / 10);
}

int countHoles(const char *str) {
    if (*str == '\0') return 0;
    return holesInChar(*str) + countHoles(str + 1);
}

int main() {
    char choice;
    cout << "Enter 'd' for number or 's' for string: ";
    cin >> choice;

    if (choice == 'd') {
        int num;
        cout << "Enter number: ";
        cin >> num;
        cout << countHoles(num) << " holes" << endl;
    }
    else if (choice == 's') {
        char str[100];
        cout << "Enter string (uppercase letters only): ";
        cin >> str;
        cout << countHoles(str) << " holes" << endl;
    }
    else {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}
