#include <iostream>
#include "DiagonalMatrix.hpp"
using namespace std;

DiagonalMatrix::DiagonalMatrix(const int size) : SquareMatrix(size) {}
DiagonalMatrix::DiagonalMatrix(DiagonalMatrix const& other) : SquareMatrix(other) {}

DiagonalMatrix DiagonalMatrix::operator+(const DiagonalMatrix& other) const {
    int n = getRows();
    DiagonalMatrix result(n);
    for (int i = 0; i < n; ++i) {
        result.setElement(i, i, getElement(i, i) + other.getElement(i, i));
    }
    return result;
}

DiagonalMatrix DiagonalMatrix::operator-(const DiagonalMatrix& other) const {
    int n = getRows();
    DiagonalMatrix result(n);
    for (int i = 0; i < n; ++i) {
        result.setElement(i, i, getElement(i, i) - other.getElement(i, i));
    }
    return result;
}

DiagonalMatrix DiagonalMatrix::operator*(const DiagonalMatrix& other) const {
    int n = getRows();
    DiagonalMatrix result(n);
    for (int i = 0; i < n; ++i) {
        result.setElement(i, i, getElement(i, i) * other.getElement(i, i));
    }
    return result;
}

bool DiagonalMatrix::operator==(const DiagonalMatrix& other) const {
    return SquareMatrix::operator==(other);
}

double DiagonalMatrix::getElement(const int row, const int col) const {
    if (row != col) {
        return 0.0;
    }
    return SquareMatrix::getElement(row, col);
}

void DiagonalMatrix::setElement(const int row, const int col, const double value) {
    if (row != col) {
        if (value != 0.0) {
            cout << "Cannot set non-zero value to off-diagonal element of DiagonalMatrix.";
        }
        return;
    }
    SquareMatrix::setElement(row, col, value);
}
