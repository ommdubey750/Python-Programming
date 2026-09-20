'''Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.

Given Input:

remove_chars("pynative", 4)
remove_chars("pynative", 2)
'''
def remove_chars(st,n):
    print(st[n:])
st="pynative"
n=int(input("Enter the number : "))
remove_chars(st,n)
