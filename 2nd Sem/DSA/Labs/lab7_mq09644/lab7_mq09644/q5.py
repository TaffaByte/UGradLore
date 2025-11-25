def finding_multiple(lst, item):
    """
    Finds all indices of an item in a sorted list using binary and linear search.
    
    Args:
    lst (list): Sorted list of items.
    item (any): Item to search for.
    
    Returns:
    list: Indices of the item, or an empty list if not found.
    """

    # WRITE YOUR CODE HERE
    left = 0
    right = len(lst) - 1
    count = []
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == item:
            count.append(mid)
        if lst[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
            
    if len(count) != 0:
        count = []
        for i in range(len(lst)):
            if item == lst[i]:
                count.append(i)
    return count

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 17)))
    # Shoud print: [5, 6, 7, 8]

    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 34)))
    # Should print: []
     
    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 19)))
    # Should print: [9] 

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py