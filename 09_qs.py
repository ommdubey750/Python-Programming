'''Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

Exercise Purpose: This exercise introduces “Membership Testing.” By checking if a character belongs to a specific group (the vowels), you learn how to filter data based on categories. This is a fundamental step toward building text-analysis tools or spam filters.

Given Input: sentence = "Learning Python is fun!"

Expected Output: Number of vowels: 6'''
sentance="Learning Python is Fun"
print("Sentance = ",sentance)
count=0
for x in sentance:
    a=x.count("a")
    e=x.count("e")
    i=x.count("i")
    o=x.count("o")
    u=x.count("u")
    count=count+a+e+i+o+u
print("Numbers of Vowels =",count)
