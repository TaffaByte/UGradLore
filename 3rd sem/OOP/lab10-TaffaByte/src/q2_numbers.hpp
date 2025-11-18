#ifndef q2_numbers_h
#define q2_numbers_h

#include <iostream>
using namespace std;
class NumInterface
{
    protected:
    unsigned int number;
public:
    virtual void display() const = 0;
    virtual void increment() = 0;
};

class NumWhole : public NumInterface
{
    public:
    NumWhole()
    {
        number = 0;
    }
    NumWhole(unsigned int v)
    {
        number = v;
    }
    unsigned int getval() const {
        return number;
    }
    void setval(unsigned int num) {
        number = num;
    }
    void display() const override {
        cout << number;
    }
    void increment() override {
        ++number;
    }
    NumWhole operator+(const NumWhole& other) const {
        NumWhole result;
        result.setval(this->getval() + other.getval());
        return result;
    }
};

class NumComplex : public NumInterface
{
    private:
    int imaginary;
    public:
    NumComplex()
    {
        number = 0;
        imaginary = 0;
    }
    NumComplex(int real, int imag)
    {
        number = static_cast<unsigned int>(real);
        imaginary = imag;
    }
    void setreal(unsigned int r) {
        number = r;
    }
    int getimag() const {
        return imaginary;
    }
    void setimag(int imag) {
        imaginary = imag;
    }
    void display() const override {
        cout << "(" << number;
        if(imaginary >= 0) cout << "+" << imaginary;
        else cout << imaginary;
        cout << "i)";
    }
    void increment() override {
        ++number;
        ++imaginary;
    }
    NumComplex operator+(const NumComplex& other) const {
        NumComplex result;
        result.setreal(this->number + other.number);
        result.setimag(this->imaginary + other.imaginary);
        return result;
    }
};

#endif