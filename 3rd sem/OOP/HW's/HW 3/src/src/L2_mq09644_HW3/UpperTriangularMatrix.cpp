#include <iostream>
#include "UpperTriangularMatrix.hpp"
using namespace std;

UpperTriangularMatrix::UpperTriangularMatrix(const int size) : SquareMatrix(size) {}
UpperTriangularMatrix::UpperTriangularMatrix(UpperTriangularMatrix const &other) : SquareMatrix(other) {}

UpperTriangularMatrix UpperTriangularMatrix::operator+(const UpperTriangularMatrix &other) const
{
    int n = getRows();
    UpperTriangularMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            result.setElement(i, j, getElement(i, j) + other.getElement(i, j));
        }
    }
    return result;
}
UpperTriangularMatrix UpperTriangularMatrix::operator-(const UpperTriangularMatrix &other) const
{
    int n = getRows();
    UpperTriangularMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            result.setElement(i, j, getElement(i, j) - other.getElement(i, j));
        }
    }
    return result;
}
UpperTriangularMatrix UpperTriangularMatrix::operator*(const UpperTriangularMatrix &other) const
{
    int n = getRows();
    UpperTriangularMatrix result(n);
    // result(i,j) is nonzero only for i <= j
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            double sum = 0.0;
            for (int k = i; k <= j; ++k) {
                sum += getElement(i, k) * other.getElement(k, j);
            }
            result.setElement(i, j, sum);
        }
    }
    return result;
}
bool UpperTriangularMatrix::operator==(const UpperTriangularMatrix &other) const
{
    return SquareMatrix::operator==(other);
}
double UpperTriangularMatrix::getElement(const int row, const int col) const
{
    if (col < row)
    {
        return 0.0;
    }
    return SquareMatrix::getElement(row, col);
}
void UpperTriangularMatrix::setElement(const int row, const int col, const double value)
{
    if (col < row)
    {
        if (value != 0.0)
        {
            cout << "Cannot set non-zero value to lower triangular part of UpperTriangularMatrix.";
        }
        return;
    }
    SquareMatrix::setElement(row, col, value);
}
