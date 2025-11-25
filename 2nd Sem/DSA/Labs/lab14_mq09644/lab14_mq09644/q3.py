from HelperFunctions import *
from q2 import GetShortestPath
    
def GetShortestPathGrid(grid, source, destination):
    """
    Finds the shortest path from source to destination in a grid using Dijkstra's algorithm.

    Args:
        grid (list): 2D matrix with obstacles (-1) and free spaces (1).
        source (tuple): Starting grid coordinates (i, j).
        destination (tuple): Target grid coordinates (i, j).

    Returns:
        list: Shortest path as [(start, end, weight), ...], or -1 if no path exists.
    """
    
    # WRITE YOUR CODE HERE

    G = {}
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1:
                continue
            nums = []
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                numi, numj = i + x, j + y
                is_valid = True
                if numi < 0 or numi >= rows:
                    is_valid = False
                elif numj < 0 or numj >= cols:
                    is_valid = False
                elif grid[numi][numj] == -1:
                    is_valid = False
                elif is_valid:
                    nums.append(((numi, numj), 1))
            G[(i, j)] = nums
    return GetShortestPath(G, source, destination)



#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    grid =[[1, 1, 1], [-1, 1, 1], [1, -1, 1]]
    source = (0, 0)
    destination = (2, 2)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print ANY ONE of the below shortest paths:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1), ((1, 1), (1, 2), 1), ((1, 2), (2, 2), 1)]
    [((0, 0), (0, 1), 1), ((0, 1), (0, 2), 1), ((0, 2), (1, 2), 1), ((1, 2), (2, 2), 1)]
    '''

    grid = [[1, 1], [-1, 1]]
    source = (0, 0)
    destination = (1, 1)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py