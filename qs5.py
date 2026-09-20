'''Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.

Exercise Purpose: This exercise will help you learn about memory efficiency and Python’s special tuple unpacking feature. In other languages like C or Java, you need a temporary variable to swap values safely. In Python, you can swap values in one line without risking data loss.

Given Input: a = 5, b = 10

'''
a=5
b=10
print("Before Swap : a =",a,",","b =",b)
b=b-a
a=a+b
print("After Swap : a =",a,",","b =",b)