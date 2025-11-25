def update_record(student_records, ID, record_title, data):
    """
    Updates a student's record based on the given ID and record title.
    
    Args:
    students_records (list): Sorted list of student records (tuples).
    ID (str): Student ID to update.
    record_title (str): The field to update ('ID', 'Email', 'Mid1', 'Mid2').
    data (str/int): New data to set for the specified field.
    
    Returns:
    str: Message indicating the result ('Record updated', 'ID cannot be updated', or 'Record not found').
    """

    # WRITE YOUR CODE HERE

    # To copy with same spelling: 
    # ”ID” ”Email” ”Mid1” ”Mid2”
    hmap= {"Email": 1, "Mid1": 2, "Mid2": 3}
    if record_title == "ID":
        return 'ID cannot be updated'
    left = 0
    right = len(student_records) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if student_records[mid][0] == ID:
            lst = list(student_records[mid])
            lst[hmap[record_title]] = data
            lst = tuple(lst)
            student_records[mid] = lst
            return "Record updated"
        if student_records[mid][0] < ID:
            left = mid + 1
        else:
            right = mid - 1
    return "Record not found"
    

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'randomID', 'Mid2', 50))
    # Should print: 'Record not found'
    print(student_records)
    ''' Should print: [
        ('aa02822', 'ea02822', 80, 65),
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    print()

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'ea02822@st.habib.edu.pk', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'ea02822', 'Email', 'updated@gmail.com'))
    # Should print: 'Record updated'
    print(student_records)
    '''Should print: [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    print()

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'fa08877', 'ID', 'change01'))
    # Should print: 'ID cannot be updated'
    print(student_records)
    ''' Should print: [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py