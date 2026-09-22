'''Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.

Given Input:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]'''
def Function():
    first_num_X=numbers_x[0:1]
    last_num_X=numbers_x[4:]
    first_num_Y=numbers_y[0:1]
    last_num_Y=numbers_y[4:]
    if first_num_X==last_num_X:
        print(f"Given List : {numbers_x} | Result is True")
    else:
        print(f"Given List : {numbers_x} | Result is False")
    if first_num_Y==last_num_Y:
        print(f"Given List : {numbers_y} | Result is True")
    else:
        print(f"Given List : {numbers_y} | Result is False")
numbers_x=[10,20,30,40,10]
numbers_y=[75,65,35,75,30]
Function()
