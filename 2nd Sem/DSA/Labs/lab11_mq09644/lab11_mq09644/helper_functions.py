import csv
import math

###########################################################################################
############################# PASTE YOUR LAB10 FUNCTIONS HERE #############################

def addNodes(G, nodes) -> None:
    """Add nodes to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be added to the graph
    """

    # WRITE YOUR CODE HERE
    for k in nodes:
        G[k] = []



def addEdges(G, edges, directed: bool = False) -> None:
    """Add edges to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    edges :
        A list of edges to be added to the graph
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False
    """

    # WRITE YOUR CODE HERE
    if directed:
        for i in edges:
            G[i[0]].append((i[1], i[2]))
    else:
        for i in edges:
            G[i[0]].append((i[1], i[2]))
            G[i[1]].append((i[0], i[2]))

def listOfNodes(G):
    """Get the list of nodes in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A list of nodes in the graph
    """

    # WRITE YOUR CODE HERE
    return list(G.keys())


def listOfEdges(G, directed: bool = False):
    """Get the list of edges in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False

    Returns
    -------
        A list of edges in the graph
    """

    # WRITE YOUR CODE HERE
    lst = []
    if directed:
        for k, v in G.items():
            for i in v:
                i = list(i)
                i.insert(0, k)
                i = tuple(i)
                lst.append(i)
        return lst
    else:
        for k, v in G.items():
            for i in v:
                i = list(i)
                i.insert(0, k)
                i = tuple(i)
                lst.append(i)
                tnode = i[1]
                del G[tnode][0]
        return lst
        


def getNeighbours(G, node):
    """Get the neighbours of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose neighbours are

    Returns
    -------
        A list of neighbours of the node
    """

    # WRITE YOUR CODE HERE
    if node in G:
        return [i for i, j in G[node]]


def getNearestNeighbor(G, node):
    """Get the nearest neighbor of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose nearest neighbor

    Returns
    -------
        The nearest neighbor of the node
    """

    # WRITE YOUR CODE HERE
    if node not in G or not G[node]:
        return None
    best_edge = G[node][0]
    for edge in G[node]:
        if edge[1] < best_edge[1]:
            best_edge = edge
    return best_edge[0]


def removeNode(G, node) -> None:
    """Remove a node from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    del G[node]
    for v in G.values():
        for i, j in enumerate(v):
            if j[0] == node:
                del v[i]


def removeNodes(G, nodes) -> None:
    """Remove nodes from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    for node in nodes:
        del G[node]
        for v in G.values():
            for i, j in enumerate(v):
                if j[0] == node:
                    del v[i]


def displayGraph(G) -> None:
    """Display the graph in a human-readable format

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    print(G)




##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################


def in_out_degree(G):
    """In and out degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the in and out degree of each node
    """

    # WRITE YOUR CODE HERE

    d = {}

    for k, v in G.items():
        key = k
        edges = v
        d[key] = (0, len(edges))

    for i in G.values():
        for j in range(len(i)):
            toop = list(d[i[j][0]])
            toop[0] += 1
            d[i[j][0]] = tuple(toop)

    return d


def degree(G):
    """Degree of an undirected graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the degree of each node
    """

    # WRITE YOUR CODE HERE

    d = {}

    for k, v in G.items():
        d[k] = len(v)

    return d

def getInNeighbors(G, node):
    """In neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose in neighbors

    Returns
    -------
        A list of in neighbors of the node
    """

    # WRITE YOUR CODE HERE

    lst = []

    for k, v in G.items():
        for i in v:
            if i[0] == node:
                lst.append(k)

    return lst


def getOutNeighbors(G, node):
    """Out neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose out neighbors

    Returns
    -------
        A list of out neighbors of the node
    """

    # WRITE YOUR CODE HERE

    temp = G[node]
    lst = []

    for i in temp:
        lst.append(i[0])

    return lst


def isNeighbor(G, node1, node2):
    """Returns True if Node2 is a neighbor of Node1 in a directed graph G.

    Parameters
    ----------
    G : dict
        A directed graph as an adjacency list.
    Node1 : any
        The node to check outgoing edges from.
    Node2 : any
        The node to check as a neighbor of Node1.

    Returns
    -------
    bool
        True if there is an edge from Node1 to Node2, False otherwise.
    """

    # WRITE YOUR CODE HERE

    if node1 not in G:
        return False

    for i in G[node1]:
        if i[0] == node2:
            return True

    return False


def initialize_matrix(rows, cols):
    """Initialize a matrix with -1

    Parameters
    ----------
    rows : int
        number of rows
    cols : int
        number of columns

    Returns
    -------
    list[list[int]]
        A matrix with -1
    """
    # WRITE YOUR CODE HERE

    return [[-1 for i in range(cols)] for j in range(rows)]


def adjlst_to_adj_matrix(G):
    """Convert adjacency list to adjacency matrix

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        An adjacency matrix of the graph
    """

    # WRITE YOUR CODE HERE

    nlst = listOfNodes(G)
    rows = cols = len(G)
    mat = initialize_matrix(rows, cols)

    for i, j in enumerate(G):
        for k in G[j]:
            index = nlst.index(k[0])
            mat[i][index] = k[1]

    return mat


def csv_to_adj_list(filename: str):
    """Convert CSV to adjacency list

    Parameters
    ----------
    filename : str
        The name of the CSV file

    Returns
    -------
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE

    with open(filename, 'r') as file:
        rows = []
        for i in csv.reader(file):
            rows.append(i)

    G = {}
    for i in rows[0][1:]:
        G[i] = []

    for i in range(1, len(rows)):
        colindex = 1
        for j in rows[0][1:]:
            if rows[i][colindex] != '-1' and rows[i][colindex] != '0':
                G[rows[i][0]].append((j, int(rows[i][colindex])))
            colindex += 1

    return G



#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
# Visible Testcases are available in main_helper_functions.py               #
#############################################################################

if __name__ == "__main__":
    import main_helper_functions

    main_helper_functions.main()


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest tests/test_helper_functions.py