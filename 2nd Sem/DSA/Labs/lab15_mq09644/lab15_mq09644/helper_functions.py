def insert(bst, key):
    """
    Inserts key in a bst.

    Args:
        bst (dictionary): The bst in which we insert the key.
        key (int): The key to insert.

    Returns:
        None
    """

    # WRITE YOUR CODE HERE
    if bst == {}:
        bst["value"] = key
        bst["left"]= {}
        bst["right"]= {}
    elif key < bst["value"]:
        insert(bst["left"], key)
    elif key > bst["value"]:
        insert(bst["right"], key)
   


def exist(bst, key):
    """
    Checks if key exists in a bst.

    Args:
        bst (dictionary): The bst in which we find the key.
        key (int): The key to find.

    Returns:
        bool: True if the key exists, False otherwise.
    """

    # WRITE YOUR CODE HERE
    if bst == {}:
        return False
    elif key < bst["value"]:
        return exist(bst["left"], key)
    elif key > bst["value"]:
        return exist(bst["right"], key)
    elif key == bst["value"]:
        return True 
    
        


def minimum(bst, starting_node):
    """
    Get the node with min value i.e. entire subtree

    Args:
        bst (dictionary): The bst in which we find the node with min value.
        starting_node (int): The key from which we start finding the min value.

    Returns:
        dict: returns the minimum node in the BST from the starting node
    """

    # WRITE YOUR CODE HERE
    current  = bst
    while current != {} and current["value"] != starting_node:
        if starting_node < current["value"]:
            current = current["left"]
        else:
            current= current["right"]
    while current['left'] != {}:
        current = current["left"]
    return current 

     

def maximum(bst,starting_node):
    """
    Get the node with max value i.e. entire subtree

    Args:
        bst (dictionary): The bst in which we find the node with max value.
        starting_node (int): The key from which we start finding the max value.

    Returns:
        dict: returns the maximum node in the BST from the starting node
    """

    # WRITE YOUR CODE HERE
    current  = bst
    while current != {} and current["value"] != starting_node:
        if starting_node < current["value"]:
            current = current["left"]
        else:
            current= current["right"]
    while current['right'] != {}:
        current = current["right"]
    return current 


def inorder_traversal(bst, res):
    """
    Perform the inorder_traversal on bst

    Args:
        bst (dictionary): The bst on which we perform the inorder_traversal
        res (list): the output list after traversal

    Returns:
        None
        Note: Update the res in-place.
    """

    # WRITE YOUR CODE HERE
    if bst =={}:
        return 
    inorder_traversal(bst["left"], res)
    res.append(bst["value"])
    inorder_traversal(bst["right"], res)


def preorder_traversal(bst, res):
    """
    Perform the preorder_traversal on bst

    Args:
        bst (dictionary): The bst on which we perform the preorder_traversal
        res (list): the output list after traversal

    Returns:
        None
        Note: Update the res in-place.
    """

    # WRITE YOUR CODE HERE
    if bst =={}:
        return 
    res.append(bst["value"])
    preorder_traversal(bst["left"], res)
    preorder_traversal(bst["right"], res)
    
    


def postorder_traversal(bst, res):
    """
    Perform the postorder_traversal on bst

    Args:
        bst (dictionary): The bst on which we perform the postorder_traversal
        res (list): the output list after traversal

    Returns:
        None
        Note: Update the res in-place.
    """
    
    # WRITE YOUR CODE HERE
    if bst =={}:
        return 
    postorder_traversal(bst["left"], res)
    postorder_traversal(bst["right"], res)
    res.append(bst["value"])


def successor(BST, key, successor_node=None):    
    """
    Find the successor of a key in bst

    Args:
        BST (dictionary): The bst on which we find the successor.
        key (int): The key whose successor we need to find.
        succssor_node (int): None by default
        
    Returns:
        int: successor of the key
    """
    
    # WRITE YOUR CODE HERE
    if BST == {}:
        return successor_node
    if BST["value"] == key:
        if BST["right"] != {}:
            successor_node = BST["right"]["value"]
            x = minimum(BST, successor_node)
            return x["value"]
        if successor_node is None:
            return None
        return successor_node["value"]
    elif BST['value'] <key:
        return successor(BST["right"], key, successor_node)
    else:
        successor_node = BST
        return successor(BST["left"], key, successor_node)





    


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    
    bst = {}
    key = 5
    insert(bst, key)
    print(bst)
    ''' Should print:
        {
            "value": 5, 
            "left": {}, 
            "right": {}
        }
   '''
    
    bst = {"value": 10, "left": {}, "right": {}}
    key = 5
    insert(bst, key)
    print(bst)
    ''' Should print: 
        {
            "value": 10,
            "left": {
                "value": 5,
                "left": {},
                "right": {}
                    }, 
            "right": {}
        }
    '''
  
    print('-------------------------------------------------------------------')

    bst = {}
    key = 5
    result = exist(bst, key)
    print(result)
    ''' Should print:   False '''
    
    bst = {"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {}}
    key = 5
    result = exist(bst, key)
    print(result)
    ''' Should print:   True '''
    
    print('-------------------------------------------------------------------')
    
    G = {'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}
    
    starting_node = 89
    result = minimum(G, starting_node)
    print(result)
    ''' Should print: 
        {
            'value': 89, 
            'left': {}, 
            'right': {
                'value': 94,
                'left': {},
                'right': {}
                }
        }
    '''
    starting_node = 50
    result = minimum(G, starting_node)
    print(result)
    ''' Should print: 
        {
            'value': 4,
            'left': {},
            'right': {}
        }
    '''

    print('-------------------------------------------------------------------')
    
    starting_node = 61
    result = maximum(G, starting_node)
    print(result)
    ''' Should print:
        {
            'value': 66,
            'left': {},
            'right': {}
        }
    '''
    
    starting_node = 68
    result = maximum(G, starting_node)
    print(result)
    ''' Should print: 
        {
            'value': 94,
            'left': {},
            'right': {}
        }
    '''

    print('-------------------------------------------------------------------')
    
    G1 = {"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {"value": 15, "left": {}, "right": {}}}
    G2 = {"value": 20, "left": {"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {}}, 
          "right": {"value": 30, "left": {}, "right": {}}}

    res = []
    inorder_traversal(G1, res)
    print(res)
    ''' Should print:   [5, 10, 15] '''
    
    res = []
    inorder_traversal(G2, res)
    print(res)
    ''' Should print:   [5, 10, 20, 30] '''

    print('-------------------------------------------------------------------')
    
    res = []
    result = preorder_traversal(G1, res)
    print(res)
    ''' Should print:    [10, 5, 15] '''
    
    res = []
    result = preorder_traversal(G2, res)
    print(res)
    ''' Should print:   [20, 10, 5, 30] '''
    
    print('-------------------------------------------------------------------')
    
    res = []
    result = postorder_traversal(G1, res)
    print(res)
    ''' Should print:   [5, 15, 10] '''

    res = []
    result = postorder_traversal(G2, res)
    print(res)
    ''' Should print:   [5, 10, 30, 20] '''   
    
    print('-------------------------------------------------------------------')
    
    key = 5
    result = successor(G1, key)
    print(result)
    ''' Should print:   10 '''
    # 
    
    key = 10
    result = successor(G1, key)
    print(result)
    ''' Should print:   15 '''
    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_helper_functions.py