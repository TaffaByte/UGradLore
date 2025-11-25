def compute_profit(stock_info):
    """
    Calculates total profit or loss from stock transactions.

    Parameters:
    stocks (list of tuples): Each tuple contains (purchase date, purchase price, shares, symbol, current price).

    Returns:
    float: Total profit or loss, rounded to two decimal places.
    """
    
    # WRITE YOUR CODE HERE
    shares = 0
    st = 0
    end = 0
    profit = 0
    t = stock_info
    for i in range(len(stock_info)):
        shares = t[i][2]
        st = t[i][1]
        end = t[i][4]
        sol = shares*(end - st)
        profit += sol
    return round(profit, 2)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(compute_profit([
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19), 
        ('25-Jan-2001', 42.1, 75, 'EK', 34.87), 
        ('25-Jan-2001', 37.58, 100, 'GM', 37.58)
    ]))
    # Should print: 1101.0

    print(compute_profit([
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19)
    ]))
    # Should print: 1643.25

    print(compute_profit([
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19), 
        ('25-Jan-2001', 42.1, 75, 'EK', 34.87), 
        ('25-Jan-2001', 37.58, 100, 'GM', 37.58), 
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19), 
        ('25-Jan-2001', 42.1, 75, 'EK', 34.87), 
        ('25-Jan-2001', 37.58, 100, 'GM', 37.58)
    ]))
    # Should print: 2202.0

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py