#include <iostream>
using namespace std;

class MyStack
{
private:
    int *stackPtr;
    int count;
    int maxCount;

public:
    MyStack(int s)
    {
        maxCount = s;
        count = -1;
        stackPtr = new int[s];
    }

    ~MyStack()
    {
        delete[] stackPtr;
    }

    void push(int data)
    {
        if (count < maxCount)
        {
            count++;
            *(stackPtr + count) = data;
        }
        else
            cout << "Stack Full!" << endl;
    }

    int pop()
    {
        if (!isempty())
        {
            int popVal = *(stackPtr + count);
            count--;
            return popVal;
        }
        else
        {
            cout << "Error! Stack is empty!" << endl;
        }
        return -1;
    }

    int top()
    {
        if (!isempty())
        {
            return *(stackPtr + count);
        }
        else
            return -1;
    }

    bool isempty()
    {
        if (count < 0)
        {
            return true;
        }
        else
            return false;
    }
};

int main()
{
    MyStack stack(10);
    stack.push(1);
    stack.push(2);
    stack.push(3);
    cout << stack.pop() << endl;
    cout << stack.pop() << endl;
    cout << stack.pop() << endl;
    cout << stack.pop() << endl;
}