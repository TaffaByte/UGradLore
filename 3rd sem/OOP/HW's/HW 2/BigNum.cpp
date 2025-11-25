#include <iostream>
#include <vector>
#include <string>
#include "BigNum.h"
#include <algorithm>
#include <fstream>

/*
Mustafa Farhan Qureshi
mq09644
L2 - Nadia Nasir
used shift + alt + f to format
*/

using namespace std;

BigNum::BigNum()
{
    minus = false;
    number.push_back('0');
}

BigNum::BigNum(const BigNum &bigNum)
{
    number = bigNum.number;
    minus = bigNum.minus;

    if (number.size() == 1 && number[0] == '0') // zero should never be negative
    {
        minus = false;
    }
}

BigNum::BigNum(const string &numStr)
{
    minus = false;
    number.clear();

    if (numStr.empty()) // handles empty string
    {
        number.push_back('0');
        return;
    }

    int start = 0;
    bool isNegative = false;

    if (numStr[0] == '-') // handle negative sign
    {
        start = 1;
        isNegative = true;
    }

    // empty string or single sign is invalid
    if (numStr.size() <= 1 && !isdigit(numStr[0]))
    {
        number.push_back('0');
        return;
    }

    // checks for valid digits and checks if there are special characters
    for (int i = start; i < numStr.size(); i++)
    {
        char c = numStr[i];

        // will only accept digits
        if (!isdigit(c))
        {
            number.push_back('0');
            return;
        }

        // checks for consecutive signs at the start
        if (i <= 1 && (c == '+' || c == '-') && (numStr[i - 1] == '+' || numStr[i - 1] == '-'))
        {
            number.push_back('0');
            return;
        }
    }

    // skip leading zeros and stores valid digits
    bool nonZeroFound = false;
    for (int i = start; i < numStr.size(); i++)
    {
        if (numStr[i] != '0')
        {
            nonZeroFound = true;
        }
        if (nonZeroFound)
        {
            number.push_back(numStr[i]);
        }
    }

    // if all zeros or no valid digits found, will set to zero
    if (number.empty())
    {
        number.push_back('0');
    }

    // set the sign (only if the number is not zero)
    minus = isNegative && !(number.size() == 1 && number[0] == '0');
}

BigNum::BigNum(const int num)
{
    minus = (num < 0);
    string x = to_string(abs(num));
    for (char c : x)
    {
        if (c != '-')
        { // skips the negative sign if present
            number.push_back(c);
        }
    }

    if (number.size() == 1 && number[0] == '0') // zero should never be negative
    {
        minus = false;
    }
}

BigNum::~BigNum()
{
    clear();
}

void BigNum::input()
{
    number.clear();
    string input1;
    for (int i = 0; i < input1.size(); i++)
    {
        number.push_back(input1[i]);
    }
}

void BigNum::print()
{
    if (minus)
        cout << '-';

    int firstGroupSize = number.size() % 3; // calculating the position for the first comma
    if (firstGroupSize == 0)
        firstGroupSize = 3;

    // hence we print the first group
    for (int i = 0; i < firstGroupSize; i++)
    {
        cout << number[i];
    }
    // printing the rest with commas
    for (int i = firstGroupSize; i < number.size(); i++)
    {
        if ((i - firstGroupSize) % 3 == 0)
            cout << ',';
        cout << number[i];
    }

    cout << endl;
}

void BigNum::inputFromFile(const string &fileName)
{
    ifstream file(fileName);
    number.clear();
    minus = false;

    string line;
    if (getline(file, line))
    {
        BigNum temp(line); // creating a new BigNum from the string
        number = temp.number;
        minus = temp.minus;
    }
    else
    {
        number.push_back('0'); // if file empty or error, sets it to 0
    }
    file.close();
}

void BigNum::printToFile(const string &fileName)
{
    ofstream file(fileName);

    if (minus && !(number.size() == 1 && number[0] == '0'))
    {
        file << '-';
    }
    for (char digit : number) // printing all the digits, decided not to use commas here
    {
        file << digit;
    }

    file << endl;
    file.close();
}

void BigNum::copy(const BigNum &bigNum)
{
    number = bigNum.number;
    minus = bigNum.minus;

    if (number.size() == 1 && number[0] == '0') // zero shouldnt be negativ
    {
        minus = false;
    }
}

void BigNum::operator=(const BigNum &bigNum)
{
    copy(bigNum);
}

void BigNum::clear()
{
    number.clear();
    minus = false;
}

void BigNum::zerofy()
{
    number.clear();
    number.push_back('0');
    minus = false; // zero will always be positive
}

void BigNum::increment()
{
    int endptr = number.size() - 1;
    if (!minus)
    {
        number[endptr]++;
        while (endptr >= 0 && number[endptr] > '9')
        {
            number[endptr] = '0';
            if (endptr > 0)
                number[endptr - 1]++;
            else
                number.insert(number.begin(), '1');
            endptr--;
        }
    }
    else
    {
        number[endptr]--;
        while (endptr >= 0 && number[endptr] < '0')
        {
            number[endptr] = '9';
            if (endptr > 0)
                number[endptr - 1]--;
            endptr--;
        }
        while (number.size() > 1 && number[0] == '0') // remove the leading zeros
            number.erase(number.begin());
    }
}

BigNum BigNum::add(const BigNum &other)
{
    BigNum result;
    result.number.clear();

    if (minus != other.minus) // checks if signs are different
    {
        bool thisLarger; // checks which absolute value is larger
        if (number.size() != other.number.size())
        {
            thisLarger = number.size() > other.number.size();
        }
        else
        { // same size, will cimpare digit by digit
            thisLarger = false;
            for (int i = 0; i < number.size(); i++)
            {
                if (number[i] > other.number[i])
                {
                    thisLarger = true;
                    break;
                }
                if (number[i] < other.number[i])
                {
                    break;
                }
            }
        }

        int borrow = 0;                                    // borrow val for subtraction
        const BigNum &larger = thisLarger ? *this : other; // used ternary operators for readability
        const BigNum &smaller = thisLarger ? other : *this;

        int j = larger.number.size() - 1;
        int k = smaller.number.size() - 1;

        while (j >= 0)
        {
            int diff = (larger.number[j] - '0') - borrow;

            if (k >= 0)
            {
                diff -= (smaller.number[k] - '0');
                k--;
            }

            if (diff < 0)
            {
                diff += 10;
                borrow = 1;
            }
            else
            {
                borrow = 0;
            }

            result.number.insert(result.number.begin(), diff + '0');
            j--;
        }

        while (result.number.size() > 1 && result.number[0] == '0') // remove leading zeros
        {
            result.number.erase(result.number.begin());
        }

        if (thisLarger)
        {
            result.minus = minus; // use this object's sign
        }
        else
        {
            result.minus = other.minus; // use other's sign
        }

        if (result.number.size() == 1 && result.number[0] == '0') // just in case of zero
        {
            result.minus = false;
        }

        return result;
    }

    // both the numbers have the same sign, performs addition of abs values
    int carry = 0;
    int x = number.size() - 1;
    int y = other.number.size() - 1;

    while (x >= 0 || y >= 0 || carry)
    {
        int sum = carry;

        if (x >= 0)
        {
            sum += number[x] - '0';
            x--;
        }
        if (y >= 0)
        {
            sum += other.number[y] - '0';
            y--;
        }

        carry = sum / 10;
        sum = sum % 10;

        result.number.insert(result.number.begin(), sum + '0');
    }
    result.minus = minus; // keeps the common sign

    // checks for zero result
    if (result.number.size() == 1 && result.number[0] == '0')
    {
        result.minus = false;
    }

    return result;
}

BigNum BigNum::add(const int num)
{
    BigNum other(num);
    return add(other);
}

void BigNum::compoundAdd(const BigNum &other)
{
    BigNum result = add(other);
    number = result.number;
    minus = result.minus;
}

void BigNum::compoundAdd(const int num)
{
    BigNum other(num);
    compoundAdd(other);
}

void BigNum::decrement()
{
    if (number.size() == 1 && number[0] == '0')
    {
        // decrementing 0 will give us -1
        minus = true;
        number[0] = '1';
        return;
    }

    if (!minus) // for positive numbers
    {
        int endptr = number.size() - 1;
        number[endptr]--;

        while (endptr >= 0 && number[endptr] < '0')
        {
            number[endptr] = '9';
            if (endptr > 0)
            {
                number[endptr - 1]--;
            }
            endptr--;
        }

        // removes leading zeros
        while (number.size() > 1 && number[0] == '0')
        {
            number.erase(number.begin());
        }
    }
    else // for negative numbers
    {
        // decrementing will make it more negative
        int endptr = number.size() - 1;
        number[endptr]++;

        while (endptr >= 0 && number[endptr] > '9')
        {
            number[endptr] = '0';
            if (endptr > 0)
            {
                number[endptr - 1]++;
            }
            else
            {
                // adds a new digit
                number.insert(number.begin(), '1');
            }
            endptr--;
        }
    }

    // if num becomes zero, sign will reset to positive
    if (number.size() == 1 && number[0] == '0')
    {
        minus = false;
    }
}

BigNum BigNum::subtract(const BigNum &other)
{
    BigNum result;
    result.number.clear();

    if (other.minus) // handle nums with signs
    {
        // a - (-b) = a + b
        BigNum temp = other;
        temp.minus = false;
        return add(temp);
    }
    if (minus)
    {
        // (-a) - b = -(a + b)
        BigNum temp = *this;
        temp.minus = false;
        result = temp.add(other);
        result.minus = true;
        return result;
    }

    // both numbers are positive, compares their size
    const BigNum *larger = this;
    const BigNum *smaller = &other;
    bool resultNegative = false;

    if (number.size() < other.number.size())
    {
        larger = &other;
        smaller = this;
        resultNegative = true;
    }
    else if (number.size() == other.number.size()) // same size, will compares digit by digit
    {
        for (int k = 0; k < number.size(); k++)
        {
            if (number[k] < other.number[k])
            {
                larger = &other;
                smaller = this;
                resultNegative = true;
                break;
            }
            else if (number[k] > other.number[k])
            {
                break;
            }
        }
    }

    int borrow = 0; // borrow val for subtraction
    int i = larger->number.size() - 1;
    int j = smaller->number.size() - 1;

    while (i >= 0)
    {
        int digit = (larger->number[i] - '0') - borrow;

        if (j >= 0)
        {
            digit -= (smaller->number[j] - '0');
            j--;
        }

        if (digit < 0)
        {
            digit += 10;
            borrow = 1;
        }
        else
        {
            borrow = 0;
        }

        result.number.insert(result.number.begin(), digit + '0');
        i--;
    }

    // remove leading zeros
    while (result.number.size() > 1 && result.number[0] == '0')
    {
        result.number.erase(result.number.begin());
    }

    // if result is zero, flag will be false as num is not negative
    if (result.number.size() == 1 && result.number[0] == '0')
    {
        result.minus = false;
    }
    else
    {
        result.minus = resultNegative;
    }

    return result;
}

BigNum BigNum::subtract(const int num)
{
    BigNum other(num);
    return subtract(other);
}

void BigNum::compoundSubtract(const BigNum &other)
{
    BigNum result = subtract(other);
    number = result.number;
    minus = result.minus;
}

void BigNum::compoundSubtract(const int num)
{
    BigNum other(num);
    compoundSubtract(other);
}

BigNum BigNum::multiply(const BigNum &other)
{
    BigNum result;
    result.number.clear();
    for (int i = 0; i < number.size() + other.number.size(); i++)
    {
        result.number.push_back('0');
    }

    result.minus = (minus != other.minus); // sign handling

    for (int i = number.size() - 1; i >= 0; i--)
    {
        int carry = 0;
        for (int j = other.number.size() - 1; j >= 0; j--)
        {
            int mul = (number[i] - '0') * (other.number[j] - '0') + (result.number[i + j + 1] - '0') + carry;
            carry = mul / 10;
            result.number[i + j + 1] = (mul % 10) + '0';
        }
        result.number[i] += carry;
    }

    // removes the leading zeros
    while (result.number.size() > 1 && result.number[0] == '0')
    {
        result.number.erase(result.number.begin());
    }

    // if result is zero, sign is positive
    if (result.number.size() == 1 && result.number[0] == '0')
    {
        result.minus = false;
    }

    return result;
}

BigNum BigNum::div(const BigNum &other)
{
    // checks for division by zero
    if (other.number.size() == 1 && other.number[0] == '0')
    {
        cout << "Invalid operation" << endl;
        return BigNum("0");
    }

    // handle signs
    bool resultNegative = (minus != other.minus);

    // positive nums
    BigNum dividend = *this;
    BigNum divisor = other;
    dividend.minus = false;
    divisor.minus = false;

    // if dividend is smaller than divisor, result is 0
    if (dividend.lessThan(divisor))
    {
        return BigNum("0");
    }

    // if division by 1
    if (other.number.size() == 1 && other.number[0] == '1')
    {
        BigNum result = *this;
        result.minus = resultNegative;
        return result;
    }

    // initializing for long division
    BigNum remainder;
    string quotient;

    for (char digit : dividend.number)
    {
        // bring down next digit
        remainder = remainder.multiply(BigNum("10")).add(BigNum(string(1, digit)));

        // find how many times divisor fits into remainder
        int count = 0;
        BigNum sum;

        while (!remainder.subtract(sum.add(divisor)).minus)
        {
            sum = sum.add(divisor);
            count++;
        }

        // add digit to quotient, then updates the remainder
        quotient += to_string(count);
        remainder = remainder.subtract(sum);
    }

    // removes leading zeros from quotient
    int start = 0;
    while (start < int(quotient.length()) - 1 && quotient[start] == '0')
    {
        start++;
    }
    quotient = quotient.substr(start);

    // create result and set its value
    BigNum result;
    result.number.assign(quotient.begin(), quotient.end());
    result.minus = (quotient == "0") ? false : resultNegative;

    return result;
}

BigNum BigNum::mod(const BigNum &other)
{
    // checks modulo by zero which is invalid operation
    if (other.number.size() == 1 && other.number[0] == '0')
    {
        cout << "Invalid operation" << endl;
        return BigNum("0");
    }

    // handles special case where dividend < divisor
    if (number.size() < other.number.size())
    {
        if (minus)
        {
            BigNum temp = other;
            temp.minus = false;
            BigNum result = *this;
            result.minus = false;
            return temp.subtract(result);
        }
        return *this;
    }

    if (number.size() == other.number.size())
    {
        for (int i = 0; i < number.size(); i++)
        {
            if (number[i] < other.number[i])
            {
                if (minus)
                {
                    BigNum temp = other;
                    temp.minus = false;
                    BigNum result = *this;
                    result.minus = false;
                    return temp.subtract(result);
                }
                return *this;
            }
            if (number[i] > other.number[i])
            {
                break;
            }
        }
    }

    // calculate remainder using division and multiplication
    BigNum quotient = div(other);
    BigNum divisor = other;
    divisor.minus = false; // uses absolute value of divisor
    BigNum product = quotient.multiply(divisor);
    BigNum remainder = subtract(product);

    // if the dividend was negative and remainder is non-zero, need to adjust the remainder
    if (minus && (remainder.number.size() > 1 || remainder.number[0] != '0'))
    {
        return divisor.subtract(remainder);
    }

    return remainder;
}

bool BigNum::equals(const BigNum &other)
{
    return number == other.number && minus == other.minus;
}

bool BigNum::notEquals(const BigNum &other)
{
    return !equals(other);
}

bool BigNum::lessThan(const BigNum &other)
{
    if (minus != other.minus)
    {
        return minus; // negative less than positive
    }

    if (number.size() != other.number.size())
    {
        if (minus)
        {
            return number.size() > other.number.size(); // more digits in negative means smaller
        }
        else
        {
            return number.size() < other.number.size(); // Fewer digits in positive means smaller
        }
    }

    for (int i = 0; i < number.size(); i++)
    {
        if (number[i] != other.number[i])
        {
            if (minus)
            {
                return number[i] > other.number[i]; // In negative, larger digit means smaller
            }
            else
            {
                return number[i] < other.number[i]; // In positive, smaller digit means smaller
            }
        }
    }

    return false; // if equal
}

bool BigNum::greaterThan(const BigNum &other)
{
    return !lessThan(other) && !equals(other);
}
