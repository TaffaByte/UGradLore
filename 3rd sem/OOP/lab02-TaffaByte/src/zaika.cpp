#include <iostream>
using namespace std;

int main () {
    int day;
    char fpflav;
    char fpsize;
    char spflav;
    char spsize;
    bool deal;
    int price1;
    int price2;
    int fprice;

    cout << "Enter day of week: "; cin >> day;
    cout << "Enter first pizza flavor (c/b/v/p/a): "; cin >> fpflav;
    cout << "Enter first pizza size (s/m/l): "; cin >> fpsize;
    cout << "Enter second pizza flavor (c/b/v/p/a): "; cin >> spflav;
    cout << "Enter second pizza size (s/m/l): "; cin >> spsize;

    int price[5][3] = {{800,1000,1200},
                    {900,1100,1300},
                    {700,900,1100},
                    {600,800,1000},
                    {1000,1200,1400}};
    
    cout << "You Ordered: " << endl;

    switch (fpflav) {
        case 'c':
        switch (fpsize) {
            case 's':
            price1 = price[0][0];
            cout << "- Small Chicken Pizza: " << price1 << "PKR" << endl;
            break;
            case 'm':
            price1 = price[0][1];
            cout << "- Medium Chicken Pizza: " << price1 << "PKR" << endl;
            break;
            case 'l':
            price1 = price[0][2];
            cout << "- Large Chicken Pizza: " << price1 << "PKR" << endl;
            break;
        }
        break;
        case 'b':
        switch (fpsize) {
            case 's':
            price1 = price[1][0];
            cout << "- Small Beef Pizza: " << price1 << "PKR" << endl;
            break;
            case 'm':
            price1 = price[1][1];
            cout << "- Medium Beef Pizza: " << price1 << "PKR" << endl;
            break;
            case 'l':
            price1 = price[1][2];
            cout << "- Large Beef Pizza: " << price1 << "PKR" << endl;
            break;
        }
        break;
        case 'v':
        switch (fpsize) {
            case 's':
            price1 = price[2][0];
            cout << "- Small Vegetarian Pizza: " << price1 << "PKR" << endl;
            break;
            case 'm':
            price1 = price[2][1];
            cout << "- Medium Vegetarian Pizza: " << price1 << "PKR" << endl;
            break;
            case 'l':
            price1 = price[2][2];
            cout << "- Large Vegetarian Pizza: " << price1 << "PKR" << endl;
            break;
        }
        break;
        case 'p':
        switch (fpsize) {
            case 's':
            price1 = price[3][0];
            cout << "- Small Plain Pizza: " << price1 << "PKR" << endl;
            break;
            case 'm':
            price1 = price[3][1];
            cout << "- Medium Plain Pizza: " << price1 << "PKR" << endl;
            break;
            case 'l':
            price1 = price[3][2];
            cout << "- Large Plain Pizza: " << price1 << "PKR" << endl;
            break;
        }
        break;
        case 'a':
        switch (fpsize) {
            case 's':
            price1 = price[4][0];
            cout << "- Small Assorted Pizza: " << price1 << "PKR" << endl;
            break;
            case 'm':
            price1 = price[4][1];
            cout << "- Medium Assorted Pizza: " << price1 << "PKR" << endl;
            break;
            case 'l':
            price1 = price[4][2];
            cout << "- Large Assorted Pizza: " << price1 << "PKR" << endl;
            break;
        break;
        }
    }
    switch (spflav) {
        case 'c':
        switch (spsize) {
            case 's':
            price2 = price[0][0];
            cout << "- Small Chicken Pizza: " << price2 << "PKR" << endl;
            break;
            case 'm':
            price2 = price[0][1];
            cout << "- Medium Chicken Pizza: " << price2 << "PKR" << endl;
            break;
            case 'l':
            price2 = price[0][2];
            cout << "- Large Chicken Pizza: " << price2 << "PKR" << endl;
            break;
        }
        break;
        case 'b':
        switch (spsize) {
            case 's':
            price2 = price[1][0];
            cout << "- Small Beef Pizza: " << price2 << "PKR" << endl;
            break;
            case 'm':
            price2 = price[1][1];
            cout << "- Medium Beef Pizza: " << price2 << "PKR" << endl;
            break;
            case 'l':
            price2 = price[1][2];
            cout << "- Large Beef Pizza: " << price2 << "PKR" << endl;
            break;
        }
        break;
        case 'v':
        switch (spsize) {
            case 's':
            price2 = price[2][0];
            cout << "- Small Vegetarian Pizza: " << price2 << "PKR" << endl;
            break;
            case 'm':
            price2 = price[2][1];
            cout << "- Medium Vegetarian Pizza: " << price2 << "PKR" << endl;
            break;
            case 'l':
            price2 = price[2][2];
            cout << "- Large Vegetarian Pizza: " << price2 << "PKR" << endl;
            break;
        }
        break;
        case 'p':
        switch (spsize) {
            case 's':
            price2 = price[3][0];
            cout << "- Small Plain Pizza: " << price2 << "PKR" << endl;
            break;
            case 'm':
            price2 = price[3][1];
            cout << "- Medium Plain Pizza: " << price2 << "PKR" << endl;
            break;
            case 'l':
            price2 = price[3][2];
            cout << "- Large Plain Pizza: " << price2 << "PKR" << endl;
            break;
        }
        break;
        case 'a':
        switch (spsize) {
            case 's':
            price2 = price[4][0];
            cout << "- Small Assorted Pizza: " << price2 << "PKR" << endl;
            break;
            case 'm':
            price2 = price[4][1];
            cout << "- Medium Assorted Pizza: " << price2 << "PKR" << endl;
            break;
            case 'l':
            price2 = price[4][2];
            cout << "- Large Assorted Pizza: " << price2 << "PKR" << endl;
            break;
        
        }
        break;
    break;
    }
    if (((fpflav == 'c') && (fpsize == 'm')|| (spflav == 'c') && (spsize == 'm')) && (day == 1)) {
        deal = true;
        cout << "Monday Deal Applied: Buy 1 Medium Chicken Pizza, get 1 Small Chicken Pizza free." << endl;
        fprice = price1 + price2;
        cout << "Final Bill: " << fprice << endl;
    } else if (((fpsize == 'l') || (spsize == 'l')) && (day == 2)) {
        deal = true;
        cout << "Buy 1 Large Pizza (any flavor), get 1 free (same flavor and size)" << endl;
        if (fpflav = spflav) {
            fprice = price1;
            cout << "Final Bill: " << fprice << endl;
        } else {
            fprice = price1 + price2;
            cout << "Final Bill: " << fprice << endl;
        }
    } else if ((fpsize == 's') && (spsize == 's') && (day == 3)) {
        deal = true;
        cout << "Buy 2 Small Pizzas (any flavors), get 20 percent off" << endl;
        fprice = price1 + price2;
        fprice = fprice * 0.8;
        cout << "Final Bill: " << endl;
    } else if (((fpflav == 'b') || (spflav == 'b')) && (day == 4)) {
        deal = true;
        cout << "Buy 1 Beef Pizza of any size, get 1 Small Plain Pizza free" << endl;
        fprice = price1 + price2;
        cout << "Final Bill: " << endl;
    } else if ((((fpflav == 'a') && (fpsize == 'l')) || ((spflav == 'a') && (spsize == 'l'))) && (day == 5)) {
        deal = true;
        cout << "Buy 1 Large Assorted Pizza, get 1 Medium Vegetarian Pizza free" << endl;
        fprice = price1 + price2;
        cout << "Final Bill: " << endl;
    } else if (day == 6) {
        fprice = price1 + price2;
        cout << "Final Bill: " << endl;
    } else if (((fpsize == 'm') || (spsize == 'm')) && (day == 7)) {
        deal = true;
        cout << "Buy 1 Medium Pizza (any flavor), get 1 Small Vegetarian Pizza free" << endl;
        fprice = price1 + price2;
        cout << "Final Bill: " << endl;
    }
    return 0;

}  
