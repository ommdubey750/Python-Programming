'''Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

Given Input: numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

Expected Output:

Even numbers: [12, 34, 10, 8, 2]
Odd numbers: [7, 21, 5, 3, 19]'''
def Func():
    even=[]
    odd=[]
    for i in number:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("Even Number :",even)
    print("Odd Number  :",odd)
number=[12,7,34,21,5,10,8,3,19,2]
Func()