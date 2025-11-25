#include <iostream>
#include "SquareMatrix.hpp"
using namespace std;

SquareMatrix::SquareMatrix(const int size) : Matrix(size, size) {}
SquareMatrix::SquareMatrix(SquareMatrix const& other) : Matrix(other) {}

SquareMatrix SquareMatrix::operator+(const SquareMatrix& other) const {
    int n = getRows();
    SquareMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            result.setElement(i, j, getElement(i, j) + other.getElement(i, j));
        }
    }
    return result;
}

SquareMatrix SquareMatrix::operator-(const SquareMatrix& other) const {
    int n = getRows();
    SquareMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            result.setElement(i, j, getElement(i, j) - other.getElement(i, j));
        }
    }
    return result;
}

SquareMatrix SquareMatrix::operator*(const SquareMatrix& other) const {
    int n = getRows();
    SquareMatrix result(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            double sum = 0.0;
            for (int k = 0; k < n; ++k) {
                sum += getElement(i, k) * other.getElement(k, j);
            }
            result.setElement(i, j, sum);
        }
    }
    return result;
}

bool SquareMatrix::operator==(const SquareMatrix& other) const {
    return Matrix::operator==(other);
}

double SquareMatrix::getElement(const int row, const int col) const {
    return Matrix::getElement(row, col);
}

void SquareMatrix::setElement(const int row, const int col, const double value) {
    Matrix::setElement(row, col, value);
}
