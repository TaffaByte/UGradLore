#include <iostream>
#include "LowerTriangularMatrix.hpp"
using namespace std;

LowerTriangularMatrix::LowerTriangularMatrix(const int size) : SquareMatrix(size) {}
LowerTriangularMatrix::LowerTriangularMatrix(LowerTriangularMatrix const& other) : SquareMatrix(other) {}

LowerTriangularMatrix LowerTriangularMatrix::operator+(const LowerTriangularMatrix& other) const {
    int n = getRows();
    LowerTriangularMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            result.setElement(i, j, getElement(i, j) + other.getElement(i, j));
        }
    }
    return result;
}

LowerTriangularMatrix LowerTriangularMatrix::operator-(const LowerTriangularMatrix& other) const {
    int n = getRows();
    LowerTriangularMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            result.setElement(i, j, getElement(i, j) - other.getElement(i, j));
        }
    }
    return result;
}

LowerTriangularMatrix LowerTriangularMatrix::operator*(const LowerTriangularMatrix& other) const {
    int n = getRows();
    LowerTriangularMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            double sum = 0.0;
            for (int k = j; k <= i; ++k) {
                sum += getElement(i, k) * other.getElement(k, j);
            }
            result.setElement(i, j, sum);
        }
    }
    return result;
}

bool LowerTriangularMatrix::operator==(const LowerTriangularMatrix& other) const {
    return SquareMatrix::operator==(other);
}

double LowerTriangularMatrix::getElement(const int row, const int col) const {
    if (col > row) {
        return 0.0;
    }
    return SquareMatrix::getElement(row, col);
}

void LowerTriangularMatrix::setElement(const int row, const int col, const double value) {
    if (col > row) {
        if (value != 0.0) {
            cout << "Cannot set non-zero value to upper triangular part of LowerTriangularMatrix.";
        }
        return;
    }
    SquareMatrix::setElement(row, col, value);
}