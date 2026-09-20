'''Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum'''
'''Given Input:

Case 1: number1 = 20, number2 = 30
Case 2: number1 = 40, number2 = 30
Expected Output:

The result is 600
The result is 70'''
def function(num1,num2):
    pro=num1*num2
    if pro<=1000:
        print("The Result is : ",pro)
    else:
        sum=num1+num2
        print("The Result is : ",sum)
num1=int(input("Enter the first number : "))
num2=int(input("Enter the Second number : "))
function(num1,num2)