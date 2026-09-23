'''Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.


Given Input:

Case 1: number = 121
Case 2: number = 125
'''
num=input("Enter the Number : ")
reverse_st=num[::-1]
reverse_num=int(reverse_st)
if int(num)==reverse_num:
    print(f"The Number {num} is palindrome number")
else:
    print(f"The Number {num} is not palindrome number")
