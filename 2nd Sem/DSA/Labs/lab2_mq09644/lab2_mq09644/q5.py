# Hint: Import initialize_matrix function from q1. (from q1 import initialize_matrix)
from q1 import initialize_matrix
#import math

def reduce_image(lst):
    """
    Reduces an image represented by a matrix A by applying the neighborhood sum and cube root formula.
    
    Parameters:
    A (list): 2D list representing the image (matrix).
    
    Returns:
    list: The reduced image (matrix) after applying the formula.

            
    Note: 
        * Utilize your initialize matrix function from q1.py for initializing the resultant matrix.
        * You are not allowed to use any built-in list functions.
    """

    # WRITE YOUR CODE HERE
    row = len(lst)
    cols = len(lst[0])
    arr = initialize_matrix(row, cols)
    t1 = [
        (-1,-1), (-1, 0), (-1, 1), 
        (0, -1),           (0, 1), 
        (1, -1), (1, 0),   (1, 1)
        ]
    for i in range(row):
        for j in range(cols):
            ans = 0
            for dx, dy in t1:
                ni = i + dx 
                nj = j + dy
                if 0 <= ni < row and 0 <= nj < cols:
                    ans += lst[ni][nj]
                arr[i][j] = round((ans * lst[i][j]) ** (1/3) , 3)
    return arr
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    print(reduce_image([
        [10, 20, 20], 
        [10, 10, 10], 
        [20, 10, 20]]
        ))
    # Should print: [
    #   [7.368, 10.627, 9.283], 
    #   [8.879, 10.627, 9.283], 
    #   [8.434, 8.879, 8.434]
    # ]

    print(reduce_image([
        [10, 10, 10, 10, 10], 
        [20, 20, 20, 20, 20], 
        [80, 80, 80, 80, 80], 
        [60, 60, 60, 60, 60], 
        [70, 70, 70, 70, 70]
        ]))
    # Should print: [
    #   [7.937, 9.283, 9.283, 9.283, 7.937], 
    #   [15.874, 18.371, 18.371, 18.371, 15.874], 
    #   [26.777, 31.748, 31.748, 31.748, 26.777], 
    #   [27.85, 32.46, 32.46, 32.46, 27.85], 
    #   [23.693, 28.189, 28.189, 28.189, 23.693]
    # ]

    print(reduce_image([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
        ]))
    # Should print: [
    #   [2.224, 3.362, 3.391], 
    #   [4.514, 5.848, 5.451], 
    #   [4.919, 6.283, 5.55]
    # ]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py