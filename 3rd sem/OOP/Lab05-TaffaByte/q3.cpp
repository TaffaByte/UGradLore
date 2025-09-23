#include <iostream>
using namespace std;

class Complex
{
private:
    double real;
    double imag;

public:
    Complex(double r = 0, double i = 0)
    {
        real = r;
        imag = i;
    }
    void show ()
    {
        cout << real;
        if (imag >= 0)
            cout << " + " << imag << "i" << endl;
        else
            cout << " - " << -imag << "i" << endl;
    }

    Complex add(Complex c)
    {
        return Complex(real + c.real, imag + c.imag);
    }
    Complex add(double r)
    {
        return Complex(real + r, imag);
    }

    Complex subtract(Complex c)
    {
        return Complex(real - c.real, imag - c.imag);
    }

    Complex subtract(double r)
    {
        return Complex(real - r, imag);
    }

    Complex multiply(Complex c)
    {
        cout << "Complex x Complex called (doing this for debugging)" << endl;
        return Complex((real * c.real) - (imag * c.imag), (real * c.imag) + (imag * c.real));
    }

    Complex multiply(double r)
    {
        cout << "Debuggin (complex x real called) -> multiply with real: " << real << " * " << r << " , " << imag << " * " << r << endl;
        return Complex((real * r) - (imag * r));
    }
};

int main()
{
    double real, imag;
    cin >> real >> imag;
    Complex c1 = {real, imag};
    cin >> real >> imag;
    Complex c2 = {real, imag};
    double d1;
    cin >> d1;
    Complex result;
    // showing the numbers :
    cout << "c1 : ";
    c1.show();
    cout << "c2 : ";
    c2.show();
    cout << "d1 : " << d1 << endl;
    // Check the opertions where both operands are complex
    result = c1.add(c2);
    cout << "c1 + c2 : ";
    result.show();
    result = c1.subtract(c2);
    cout << "c1 - c2 : ";
    result.show();
    result = c1.multiply(c2);
    cout << "c1 * c2 : ";
    result.show();
    // Check the opertions where one operator is complex , other is double
    result = c1.add(d1);
    cout << "c1 + d1 : ";
    result.show();
    result = c1.subtract(d1);
    cout << "c1 - d1 : ";
    result.show();
    result = c1.multiply(d1);
    cout << "c1 * d1 : ";
    result.show();
    return 0;
}