#include <iostream>
using namespace std;

// Write Your Code Here

class publication
{
protected:
    string title;
    float price;

public:
    void getdata()
    {
        cout << "Enter title: ";
        getline(cin, title);
        cout << "Enter price: ";
        cin >> price;
    }
    void putdata()
    {
        cout << "Publication Title: " << title << endl;
        cout << "Publication Price: " << price << endl;
    }
};
class book : public publication
{
private:
    int pageCount;

public:
    void getdata()
    {
        publication::getdata();
        cout << "Enter page count: ";
        cin >> pageCount;
    }
    void putdata()
    {
        publication::putdata();
        cout << "Book page Count: " << pageCount << endl;
    }
};

class tape : public publication
{
private:
    float duration;

public:
    void getdata()
    {
        publication::getdata();
        cout << "Enter duration: ";
        cin >> duration;
    }
    void putdata()
    {
        publication::putdata();
        cout << "Tape's playing time: " << duration << endl;
    }
};

int main()
{
    book b;
    tape t;
    b.getdata();
    cin.ignore();
    t.getdata();
    b.putdata();
    t.putdata();
}