from Helper_Functions import *

def nodes_of_level(G,level):
    """
    Returns a list of nodes on the given level in the graph G.

    Parameters
    ----------
    G : dict
        A directed graph represented as an adjacency list.
    level : int
        The level in the graph to find the nodes for.

    Returns
    -------
    list
        A list of nodes that are on the given level.
    """
    
    # WRITE YOUR CODE HERE
    start = listOfNodes(G)[0]
    qoo = Initialize(len(G))
    visited = []
    nodelevels = {start: 0}
    enQueue(qoo, start)
    visited.append(start)
    while not IsEmpty(qoo):
        curr = deQueue(qoo)
        for i in getNeighbors(G, curr):
            if i not in visited:
                visited.append(i)
                nodelevels[i] = nodelevels[curr] + 1
                enQueue(qoo, i)
    return [n for n, lvl in nodelevels.items() if lvl == level]


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
            's': [(1, 1), (2, 1)],
            1: [(3, 1), (4, 1), (5, 1)],
            2: [(6, 1)],
            3: [],
            4: [],
            5: [],
            6: [(7, 1)],
            7: []
    }

    print(sorted(nodes_of_level(G, 1)))     # SHOULD PRINT: [1, 2]

    print(sorted(nodes_of_level(G, 2)))     # SHOULD PRINT: [3, 4, 5, 6]

    print(sorted(nodes_of_level(G, 3)))     # SHOULD PRINT: [7]

    G = {
            'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)],
            'Austin': [('Houston', 160), ('Chicago', 900)],
            'Washington': [('Atlanta', 600)],
            'Denver': [],
            'Atlanta': [],
            'Chicago': [],
            'Houston': []
        }
    
    print(sorted(nodes_of_level(G, 1)))     # SHOULD PRINT: ['Austin', 'Denver', 'Washington']

    print(sorted(nodes_of_level(G, 3)))     # SHOULD PRINT: ['Atlanta', 'Chicago', 'Houston']


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py