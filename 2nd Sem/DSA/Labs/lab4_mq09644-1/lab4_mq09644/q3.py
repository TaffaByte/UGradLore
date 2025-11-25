# Tip: Import and use created Stack functions from q1. (from q1 import *)
from q1 import *

def balanced_braces(s):
    """
    Checks if the braces in the string are balanced using stack operations only.

    Parameters:
    s (str): The string containing braces to be checked.
    
    Returns:
    bool: True if the braces are balanced, False otherwise.

    Note:
        1. Only Stack ADT Operations are to be used in your implementation:
            ( Initialize() , push() , pop() , top() and is_empty() ).
        2. You have to use a SINGLE Stack only.
        3. You are NOT allowed to use any sort of counter to count number of brackets.
        4. You are NOT allowed to use any sort of counter to count number of opening and closing brackets.
        5. Don't use Stack ADT operations on the given string.
    """

    # WRITE YOUR CODE HERE
    stack = Initialize(len(s))
    # startbrackets = {"(": 1, "[": 2, "{": 3}
    # endbrackets = {")": 1, "]": 2, "}": 3}
    y = False
    for i in range(len(s)):
        x = top(stack)
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            push(stack, s[i])
        elif is_empty(stack):
            return False
        elif x == "(" and s[i] == ")":
            pop(stack)
            y = True
        elif x == "[" and s[i] == "]":
            pop(stack)
            y = True
        elif x == "{" and s[i] == "}":
            pop(stack)
            y = True
        else:
            return False
    return y


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(balanced_braces("()"))                    # Should print: True

    print(balanced_braces("())"))                   # Should print: False

    print(balanced_braces("{()}"))                  # Should print: True

    print(balanced_braces("{)({"))                  # Should print: False

    print(balanced_braces("{()}[]()"))              # Should print: True

    print(balanced_braces("{[}]"))                  # Should print: False

    print(balanced_braces("()()()([{])}({{[]}})"))  # Should print: False

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py