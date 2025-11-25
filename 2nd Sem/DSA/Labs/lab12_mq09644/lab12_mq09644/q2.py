from Helper_Functions import *

def check_cycles(G,lst):
    '''
    Returns True if the list of nodes forms a directed cycle in G.

    Parameters
    ----------
    G : dict
        Directed graph as an adjacency list.
    lst : list
        List of nodes to check for a cycle.

    Returns
    -------
    bool
        True if lst forms a directed cycle, False otherwise."
    '''

    # WRITE YOUR CODE HERE

    for i in range(len(lst)):
        connection = False
        for j in G[lst[i]]:
            if lst[(i+1)%len(lst)] == j[0]:
                connection = True
                break
        if connection == False:
            break
    return connection



#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
            'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
            'Austin': [('Dallas', 200), ('Houston', 160)], 
            'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
            'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
            'Atlanta': [('Washington', 600), ('Houston', 800)], 
            'Chicago': [('Denver', 1000)], 
            'Houston': [('Atlanta', 800)]
        }
    
    print(check_cycles(G, ['Dallas','Denver','Atlanta','Washington']))  # SHOULD PRINT:     True


    G = {
            'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 
            'ORD': [('MIA', 1), ('DFW', 1)], 
            'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 
            'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 
            'MIA': [('DFW', 1), ('LAX', 1)], 
            'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] 
        }
    print(check_cycles(G, ['BOS', 'MIA', 'JFK']))   # SHOULD PRINT :    False
    print(check_cycles(G, ['JFK','MIA','DFW']))     # SHOULD PRINT :    False


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py