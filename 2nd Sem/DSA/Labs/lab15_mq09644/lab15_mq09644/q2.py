from helper_functions import *

def q_2():    
    """
    Creates a bst with given keys. See manual for keys.

    Args:
      None

    Returns:
        dict: The resulting bst after inserting all keys
    """
    
    # WRITE YOUR CODE HERE
    keys =  ["begin", "do", "else", "end", "if", "then", "while"]
    bst= {}
    for key in keys:
        insert(bst,key)
    return bst


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    q_2()
    ''' Should print:
    {'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 
    'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 
    'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}
    '''


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py