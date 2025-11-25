#include <iostream>
#include <iomanip>
using namespace std;
int day;
int hours;
int mins;
int secs;

void convert24(int hours, int mins, int secs) {
    while (secs >= 60) {
        mins++;
        secs-=60;
    }
    while (mins >= 60) {
        hours++;
        mins-=60;
    }
    while (hours >= 24) {
        day++;
        hours-=24;
    }
    cout << "+" << day << ", " << setfill('0') << setw(2) << hours << ":" << setfill('0') << setw(2) << mins << ":" << setfill('0') << setw(2) << secs << endl;
}
void convert24(int mins, int secs) {
    while (secs >= 60) {
        mins++;
        secs-=60;
    }
    while (mins >= 60) {
        hours++;
        mins-=60;
    }
    cout << setfill('0') << setw(2) << hours << ":" << setfill('0') << setw(2) << mins << ":" << setfill('0') << setw(2) << secs << endl;
}
void convert24(int secs) {
    while (secs >= 60) {
        mins++;
        secs-=60;
    }
    // if (minute < 10)
     //   cout << "00:0" << minute << ":" << secs << endl;
    //else cout << "00:" << minute << ":" << secs << endl;
    cout << "00:" << setfill('0') << setw(2) << mins << ":" << setfill('0') << setw(2) << secs << endl;
}

int main() {
    cout << "Enter Hours: "; cin >> hours;
    cout << "Enter Minutes: "; cin >> mins;
    cout << "Enter Seconds: "; cin >> secs;

    if (hours > 0 || mins > 0 || secs > 0) {
        convert24(hours, mins, secs);
    } else if (hours == 0 || mins > 0 || secs > 0) {
        convert24(mins, secs);
    } else convert24(secs);
}