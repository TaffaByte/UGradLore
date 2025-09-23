#include <iostream>
using namespace std;

class TollBooth {
    private:
        unsigned int totalcars;
        unsigned int totalmoney;
    public:
        TollBooth() {
            totalcars = 0;
            totalmoney = 0;
        }
        void payingCar() {
            totalcars ++;
            totalmoney = totalmoney + 50;
        }
        void nopayCar() {
            totalcars ++;
        }
        void display() {
            cout << "Total cars passed: " << totalcars << endl;
            cout << "Total toll collected: Rs. " << totalmoney << endl;
        }
};

int main() {
    char enter;
    TollBooth toll;
    while (enter != 'q') {
        cin >> enter;
        if (enter == 'p') {
            toll.payingCar();
        } else if (enter == 'n') {
            toll.nopayCar();
        }
    }
    toll.display();
}