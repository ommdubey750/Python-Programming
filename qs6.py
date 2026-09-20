'''Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

Exercise Purpose: This exercise explores “Mathematical Accumulation.” A factorial (e.g., 5! = 5*4*3*2*1) requires you to maintain a running product across multiple iterations, which is a core pattern in scientific computing.

Given Input: number = 5

Expected Output: The factorial of 5 is 120'''
def  Factorial(num):
    res=num
    for i in range(num):
        if i==0:
            continue
        res=res*i
    print(f"The Factorial of {num} is {res}")
num=int(input("Enter the Number : "))
Factorial(num)