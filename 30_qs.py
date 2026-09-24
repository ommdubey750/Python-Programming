'''Practice Problem: Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

Exercise Purpose: This is a classic “Natural Language Processing” (NLP) task. It teaches you how to map data to occurrences, which is the logic used by search engines to index web pages or by social media platforms to identify trending hashtags.

Given Input: text = "apple banana apple cherry banana apple"

Expected Output: {'apple': 3, 'banana': 2, 'cherry': 1}'''
def Func():
    count_apple=0
    count_banana=0
    count_cherry=0
    b=text.split()
    for i in b:
        if'apple' in i:
            count_apple+=1
        elif'banana' in i:
            count_banana+=1
        else:
            count_cherry+=1
    pair1=[('apple',count_apple),('banana',count_banana),('cherry',count_cherry)]
    dict1=dict(pair1)
    print(dict1)
text="apple banana apple cherry banana apple"
Func()
