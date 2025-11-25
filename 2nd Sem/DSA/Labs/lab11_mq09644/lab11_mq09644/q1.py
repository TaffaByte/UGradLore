from helper_functions import *

def create_directed_graph():
    """
    Creates a directed graph using an adjacency list representation.

    Returns:
        dict: A dictionary representing the adjacency list of the directed graph.
    """

    # WRITE YOUR CODE HERE

    G = {1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}

    return G


def print_graph(G):
    """
    Prints the adjacency list representation of the directed graph.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        None
    """
    
    # WRITE YOUR CODE HERE

    print(G)

def in_neighbors(G):
    """
    Computes the in-neighbors of each node.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are lists of in-neighbors.
    """
    
    # WRITE YOUR CODE HERE

    d = {}

    for i in listOfNodes(G):
        d[i] = getInNeighbors(G, i)

    return d


def out_neighbors(G):
    """
    Computes the out-neighbors of each node.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are lists of out-neighbors.
    """

    # WRITE YOUR CODE HERE

    d = {}

    for i in listOfNodes(G):
        d[i] = getOutNeighbors(G, i)

    return d


def generate_adjacency_matrix(G):
    """
    Generates and returns the adjacency matrix representation of the graph.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        list: A 2D list representing the adjacency matrix of the graph.
    """
    
    # WRITE YOUR CODE HERE

    return adjlst_to_adj_matrix(G)


def check_degree_sums(G):
    """
    Checks whether the sum of in-degrees, the sum of out-degrees, 
    and the total number of edges in the graph are equal.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        bool: True if sum of in-degrees == sum of out-degrees == total number of edges, otherwise False.
    """
    
    # WRITE YOUR CODE HERE

    inn = 0
    out = 0

    for i in in_out_degree(G):
        inn += in_out_degree(G)[i][0]
        out += in_out_degree(G)[i][1]

    if inn == out == len(listOfEdges(G, True)):
        return True
    return False


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_directed_graph()

    print_graph(G)
    '''
    SHOULD PRINT:
    {1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}
    '''

    print("IN NEIGHBORS")
    print(in_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [3], 2: [1, 3], 3: [4], 4: [2, 4] }
    '''
    
    print("OUT NEIGHBORS")
    print(out_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [2], 2: [4], 3: [1, 2], 4: [3, 4] }
    '''

    print("ADJACENCY MATRIX")
    print(generate_adjacency_matrix(G))
    '''
    SHOULD PRINT:
    [[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]
    '''

    print("Sum of the in-degrees of all nodes, "
    "the sum of the out-degrees of all nodes "
    "and the total number of edges are all equal: ")
    
    print(check_degree_sums(G))
    '''
    SHOULD PRINT:
    True
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py