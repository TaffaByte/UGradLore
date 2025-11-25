#include <iostream>
using namespace std;

int main() {

    char service;
    int category;
    int row;
    int NH[12] = {0, 0, 0, 500, 900, 1600, 300, 600, 1100, 200, 450, 800};
    int CP[12] = {0, 0, 0, 550, 950, 1700, 320, 620, 1150, 220, 470, 850};
    int SC[12] = {0, 0, 0, 600, 1000, 1800, 350, 650, 1200, 250, 500, 900};
    cout << "Service: ";
    cin >> service;
    cout << "Cargo: ";
    cin >> category;
    cout << "Category: ";

    switch (service) {

        case 'U': cout << "Urgent Service, "; row = 1; 
        break;
        case 'N': cout << "Normal Service, "; row = 2; 
        break; 
        case 'E': cout << "Economy Service, "; row = 3; 
        break;
    }

    switch (category) {

        case 1: cout << "Documents" << endl; 
        break;
        case 2: cout << "Parcel < 5kg" << endl; 
        break;
        case 3: cout << "Parcel >= 5kg" << endl; 
        break;
    }

    cout << "Prices: " << NH[row * 3 + category - 1] << ", " << CP[row * 3 + category - 1] << ", " << SC[row * 3 + category - 1] << endl;
    cout << "Average Price: " << (NH[row * 3 + category - 1] + CP[row * 3 + category - 1] + SC[row * 3 + category - 1]) / 3.0 << " PKR" << endl;
    cout << "Maximum Price: " << SC[row * 3 + category - 1] << " PKR" << endl;
    cout << "Minimum Price: " << NH[row * 3 + category - 1] << " PKR" << endl;

    return 0;
}