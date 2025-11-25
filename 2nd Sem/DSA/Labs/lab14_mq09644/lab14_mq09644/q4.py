from HelperFunctions import *
from q2 import GetShortestPath

def GetShortestDistanceBetweenCities(source, destination):
    """
    Computes the shortest path between two cities using Dijkstra's algorithm.

    Reads the adjacency matrix from `connections.csv` and returns the shortest 
    path from `source` to `destination` as a list of tuples (start_city, end_city, distance), 
    or -1 if no path exists.

    Args:
        source (str): The starting city.
        destination (str): The destination city.

    Returns:
        list or int: Shortest path as a list of tuples (start_city, end_city, distance), 
                     or -1 if no path exists.
    """

    # WRITE YOUR CODE HERE
    with open('connections.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        matrix = []
        for row in csv_reader:
            matrix.append(row)
    
    col_map = {}
    G = {}
    for i, col in enumerate(header[1:]):
        col_map[i] = col
        G[col] = []
    for i, row in enumerate(matrix):
        for j in range(1, len(row)):
            weight = int(row[j])
            if weight > 0:
                s_node = col_map[i]
                t_node = col_map[j - 1]
                G[s_node].append((t_node, weight))
    return GetShortestPath(G, source, destination)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))   
    '''Should print:
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]
    '''

    print(GetShortestDistanceBetweenCities('Islamabad', 'Naran'))
    ''' Should print: 
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), 
     ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), 
     ('Kaghan', 'Naran', 22)]
    '''
    
    print(GetShortestDistanceBetweenCities("Islamabad", "Murree"))
    ''' Should print:
    [('Islamabad', 'Murree', 49)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py