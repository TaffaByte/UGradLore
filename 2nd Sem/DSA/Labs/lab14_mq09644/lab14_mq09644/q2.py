from HelperFunctions import *
from q1 import *

def GetShortestPath(graph, source, destination):
    """
    Finds the shortest path from source to destination using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary of nodes and their neighbors with edge weights.
        source (any): The starting node.
        destination (any): The target node.

    Returns:
        list: A list of (prev_node, node, weight) tuples representing the shortest path, or -1 if no path exists.
    """

    # WRITE YOUR CODE HERE
    
    if source == destination:
        return -1
    output = []
    p_queue = []
    dist = {}
    prev = {}
    for v in graph:
        prev[v] = None
        if v == source:
            dist[v] = 0
            EnQueue(p_queue, v, 0)
        else:
            dist[v] = float('inf')
            EnQueue(p_queue, v, float('inf'))
    while not IsEmpty(p_queue):
        u = DeQueue(p_queue)
        min_dist = dist[u]

        for nbr, w in graph[u]:
            upd_weight = min_dist + w
            if upd_weight < dist[nbr]:
                dist[nbr] = upd_weight
                prev[nbr] = u
                EnQueue(p_queue, nbr, upd_weight)

    if dist[destination] == float('inf'):
        return -1

    curr = destination
    while curr != source:
        prev_node = prev[curr]
        for nbr, weight in graph[prev_node]:
            if nbr == curr:
                output.insert(0, (prev_node, curr, weight))
                break
        curr = prev_node

    return output


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    graph = {
        'A': [('D', 2), ('E', 6), ('B', 7)], 
        'B': [('C', 3), ('A', 7)], 
        'C': [('B', 3), ('D', 2), ('G', 2)], 
        'D': [('A', 2), ('C', 2), ('F', 8)], 
        'E': [('A', 6), ('F', 9)], 
        'F': [('D', 8), ('E', 9), ('G', 4)], 
        'G': [('C', 2), ('F', 4)]
    }

    print(GetShortestPath(graph, 'A', 'G'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2), ('C', 'G', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'C'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'D'))
    ''' Should print:
    [('A', 'D', 2)]
    '''


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py