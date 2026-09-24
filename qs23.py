'''Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

Exercise Purpose: This exercise teaches “Algorithmic Reversal.” While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory and how to manipulate digits individually.

Given Input: number = 121

Expected Output:

Original number 121
Yes. given number is palindrome number'''
num=int(input("Enter the number : "))
num2=num
reversed_num=0
while num>0:
    remender=num%10
    reversed_num=(reversed_num*10)+remender
    num=num//10
if num2==reversed_num:
    print("This is Palindrome")
else:
    print("This is Not Palindrome")