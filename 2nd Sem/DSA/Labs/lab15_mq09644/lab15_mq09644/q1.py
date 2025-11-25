from helper_functions import *

  
def q_1a():
    """
    Creates a bst with given keys. See manual for keys.

    Args:
      None

    Returns:
        dict: The resulting bst after inserting all keys
    """

    # WRITE YOUR CODE HERE
    keys = [68, 88, 61, 89, 94, 50, 4, 76, 66, 82]
    bst = {}
    for key in keys:
        insert(bst,key)
    return bst 
    
  
def q_1b(bst):
    """
    Checks if key 50 exists in the bst.

    Args:
        bst (dictionary): The bst in which we find the key.

    Returns:
        bool: True if the key exists, False otherwise.
    """

    # WRITE YOUR CODE HERE
    return exist(bst,50)

  
def q_1c(bst):
    """
    Checks if key 49 exists in the bst.

    Args:
        bst (dictionary): The bst in which we find the key.

    Returns:
        bool: True if the key exists, False otherwise.
    """
    
    # WRITE YOUR CODE HERE
    return exist(bst,49)


def q_1d(bst):
    """
    Find the node with the minimum value in resultant Binary Search Tree from starting node = 68.

    Args:
        bst (dictionary): The bst in which we find the node with min value.

    Returns:
        dict: returns the minimum node in the BST from the starting node
    """

    # WRITE YOUR CODE HERE
    return minimum(bst, 68)


def q_1e(bst):
    """
    Find the node with the minimum value in resultant Binary Search Tree from starting node = 88.

    Args:
        bst (dictionary): The bst in which we find the node with min value.

    Returns:
        dict: returns the minimum node in the BST from the starting node
    """
    
    # WRITE YOUR CODE HERE
    return minimum(bst, 88)

  
def q_1f(bst):
    """
    Find the node with the maximum value in resultant Binary Search Tree from starting node = 68.

    Args:
        bst (dictionary): The bst in which we find the node with max value.

    Returns:
        dict: returns the maximum node in the BST from the starting node
    """
    
    # WRITE YOUR CODE HERE
    return maximum(bst, 68)

  
def q_1g(bst):
    """
    Find the node with the maximum value in resultant Binary Search Tree from starting node = 61.

    Args:
        bst (dictionary): The bst in which we find the node with max value.

    Returns:
        dict: returns the maximum node in the BST from the starting node
    """
    
    # WRITE YOUR CODE HERE
    return maximum(bst, 61)

  
def q_1h(bst):
    """
    Perform the inorder_traversal on bst

    Args:
        bst (dictionary): The bst on which we perform the inorder_traversal

    Returns:
        list: in-order traversal 
    """
    
    # WRITE YOUR CODE HERE
    res = []
    inorder_traversal(bst, res)
    return res


def q_1i(bst):
    """
    Perform the preorder_traversal on bst

    Args:
        bst (dictionary): The bst on which we perform the preorder_traversal

    Returns:
        list: preorder traversal
    """   
    
    # WRITE YOUR CODE HERE
    res = []
    preorder_traversal(bst, res)
    return res


def q_1j(bst):
    """
    Perform the postorder_traversal on bst

    Args:
        bst (dictionary): The bst on which we perform the postorder_traversal

    Returns:
        list: postorder traversal
    """

    # WRITE YOUR CODE HERE
    res =[]
    postorder_traversal(bst, res)
    return res


def q_1k(BST):
    
    """
    Find the successor of key = 76 in bst

    Args:
        BST (dictionary): The bst in which we find the successor
        
    Returns:
        int: successor of the key
    """
    
    # WRITE YOUR CODE HERE
    return successor(BST, key = 76, successor_node=None)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__": 
    
    # q_1a
    bst = q_1a()
    print(bst)
    ''' Should print: 
    {'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 
    'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 
    'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 
    'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}
    '''

    # q_1b
    res = q_1b(bst)
    print(res)
    ''' Should print:   True '''

    # q_1c
    res = q_1c(bst)
    print(res)
    ''' Should print:   False '''

    # q_1d
    res = q_1d(bst)
    print(res)
    ''' Should print:
    {'value': 4, 'left': {}, 'right': {}}
    '''

    # q_1e
    res = q_1e(bst)
    print(res)
    ''' Should print:
    {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}
    '''

    # q_1f
    res = q_1f(bst)
    print(res)
    ''' Should print:
    {'value': 94, 'left': {}, 'right': {}}
    '''

    # q_1g
    res = q_1g(bst)
    print(res)
    ''' Should print:
    {'value': 66, 'left': {}, 'right': {}}
    '''

    # q_1h
    res = q_1h(bst)
    print(res)
    ''' Should print:   [4, 50, 61, 66, 68, 76, 82, 88, 89, 94] '''

    # q_1i
    res = q_1i(bst)
    print(res)
    ''' Should print:   [68, 61, 50, 4, 66, 88, 76, 82, 89, 94] '''
    
    # q_1j
    res = q_1j(bst)
    print(res)
    ''' Should print:   [4, 50, 66, 61, 82, 76, 94, 89, 88, 68] '''
    
    # q_1k
    res = q_1k(bst)
    print(res)
    ''' Should print:   82  '''


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py