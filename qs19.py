'''Practice Problem: Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.
Given Input: income = 45000

Expected Output: Total income tax to pay is 6000
'''
def Func():
    tax_0=(10000/100)*0
    tax_10=(10000/100)*10
    tax=income-20000
    tax_20=(tax/100)*20
    total=tax_0+tax_10+tax_20
    print("Total income tax to pay is ",total)
income=int(input("Enter your Salary : "))
Func()