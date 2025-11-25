def quick_sort_rectangles(rectangle_records, low, high, column):
    """
    Sorts a list of rectangle records in-place by the specified key using QuickSort.
    Uses the lowest index as the pivot for partitioning.
    
    Parameters:
    rectangle_records (list of dict): Rectangle records to sort.
    low (int): Starting index.
    high (int): Ending index.
    record_title (str): Key to sort by ("ID", "Length", "Breadth", or "Color").
    
    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    if low < high:
        pi = PartitionMid(rectangle_records, low, high, column)
        print(rectangle_records)
        quick_sort_rectangles(rectangle_records, low, pi - 1, column)
        quick_sort_rectangles(rectangle_records, pi + 1, high, column)

def Partition(lst, low, high, column):
    pivot = low
    i = low + 1
    for j in range(low + 1,high + 1):
        if lst[j][column] <= lst[pivot][column]:
            lst[i], lst[j] = lst[j], lst[i]
            i = i + 1
    lst[pivot], lst[i - 1] = lst[i - 1], lst[pivot]
    pivot = i - 1
    return pivot

def PartitionMid(lst, low, high, column):
    pivot = low
    lst[low], lst[pivot] = lst[pivot], lst[low]
    return Partition(lst, low, high, column)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "Length")
    ''' Should print:
        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]

        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]
    '''

    print()

    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "ID")
    ''' Should print:
        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py