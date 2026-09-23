'''Practice Problem: Write a program to extract each digit from an integer in the reverse order.

Exercise Purpose: This exercise explores “Mathematical Parsing.” Instead of converting a number to a string, use the modulo operator (%) and floor division (//) to isolate digits. This is common in low-level programming and algorithm challenges where type conversion is restricted.

Given Input: number = 7536

Expected Output: 6 3 5 7'''
num=int(input("Enter the number : "))
num_st=str(num)
reversed_st=num_st[::-1]
print(int(reversed_st))