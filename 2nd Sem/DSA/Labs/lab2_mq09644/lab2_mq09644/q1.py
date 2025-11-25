def initialize_matrix(rows, cols):
    """
    Creates a matrix of size `row` x `column` with all values set to 0.

    Parameters:
    row (int): Number of rows.
    column (int): Number of columns.

    Returns:
    list: A 2D list (matrix) of 0s.

    Note: You are not allowed to use any built-in list functions.
    """
    
    # WRITE YOUR CODE HERE
    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    return arr

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(initialize_matrix(3, 3))
    # Should print: [
    #   [0, 0, 0], 
    #   [0, 0, 0], 
    #   [0, 0, 0]
    # ]

    print(initialize_matrix(2, 5))
    # Should print: [
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0]
    # ]

    print(initialize_matrix(7, 3))
    # Should print: [
    #   [0, 0, 0], 
    #   [0, 0, 0],
    #   [0, 0, 0], 
    #   [0, 0, 0], 
    #   [0, 0, 0], 
    #   [0, 0, 0], 
    #   [0, 0, 0]
    # ]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py