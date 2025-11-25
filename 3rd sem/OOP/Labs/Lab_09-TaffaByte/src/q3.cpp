#include <iostream>
using namespace std;

// Write Your Code Here
class Payment
{
protected:
	double amount;

public:
	virtual void paymentDetails()
	{
		cout << "Amount of payment: " << amount << endl;
	}
};

class CashPayment : public Payment
{
public:
CashPayment(double amt)
	{
		amount = amt;
	}
	void paymentDetails() override
	{
		cout << "Amount of cash payment: " << amount << endl;
	}
};

class CreditCardPayment : public Payment
{
private:
	string cardHolderName;
	string expiryDate;
	string cardNumber;

public:
	CreditCardPayment(double amt, string name, string expiry, string number)
	{
		amount = amt;
		cardHolderName = name;
		expiryDate = expiry;
		cardNumber = number;
	}
	void paymentDetails() override
	{
		cout << "Amount of credit card payment: " << amount << endl;
		cout << "Name on the credit card: " << cardHolderName << endl;
		cout << "Expiration Date: " << expiryDate << endl;
		cout << "Credit card Number: " << cardNumber << endl;
	}
};

int main()
{
	CashPayment cp1(75.25);
	CashPayment cp2(36.95);
	CreditCardPayment ccp1(95.15, "Smith", "12/21/2009", "321654987");
	CreditCardPayment ccp2(45.75, "James", "10/30/2008", "963852741");

	cout << "Details of Cash #1..." << endl;
	cp1.paymentDetails();

	cout << "\nDetails of Cash #2..." << endl;
	cp2.paymentDetails();

	cout << "\nDetails of Credit Card #1..." << endl;
	ccp1.paymentDetails();

	cout << "\nDetails of Credit Card #2..." << endl;
	ccp2.paymentDetails();

	return 0;
}