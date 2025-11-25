# Decrypt the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting of leaves
# Returns:
#   A tuple containing the original two numbers.
def reverse_karatsuba(data, level=0) -> tuple:

    if isinstance(data, tuple): # base case: if data will be a tuple it will return it
        return data
    
    if isinstance(data, list): # checks if first element is a list, here it will process recursively by using indexing

        left = reverse_karatsuba(data[0], level)
        right = reverse_karatsuba(data[2], level)
        level += 1

        x_cord = str(right[0]) + str(left[0])
        y_cord = str(right[1]) + str(left[1])
        z_cord = left[2] * 10
    
    return (int(x_cord), int(y_cord), int(z_cord))
    pass
    
# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (x, y).

def main(filename) -> list[tuple[int, int]]:

    op_lst = [] # list to store the output: list[tuple[int, int]]

    with open(filename, "r") as file:

        line_number = int(file.readline().strip()) # no. of lines to read

        for i in range(line_number):
            array = eval(file.readline()) # reads the array
            toop = tuple(reverse_karatsuba(array, line_number)) # calls the function to decrypt the data
            op_lst.append((toop, toop[0] * toop[1] * toop[2])) # appends the output to the list

    return op_lst
    pass

print(main("question1_divideAndConquer/input_decrypt.txt"))