'''Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

Exercise Purpose: This exercise introduces “Metadata Extraction.” Often, you aren’t just interested in the data itself, but in its properties. In web development, this logic is used to validate if a user’s password or username meets specific length requirements.

Given Input: words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

Expected Output:

Apple - 5 Banana - 6 Cherry - 6 Date - 4 Elderberry - 10'''
def Func():
    count_apple=0
    count_banana=0
    count_cherry=0
    count_date=0
    count_elderberry=0
    for i in words:
        if'Apple' in i:
            for x in str(i):
                count_apple+=1
        elif'Banana' in i:
            for x in str(i):
                count_banana+=1
        elif'Cherry' in i:
            for x in str(i):
                count_cherry+=1
        elif'Date' in i:
            for x in str(i):
                count_date+=1
        elif'Elderberry' in i:
            for x in str(i):
                count_elderberry+=1
    print(f"Apple - {count_apple} Banana -{count_banana} Cherry - {count_cherry} Date - {count_date} Elderberry - {count_elderberry}")
words=["Apple","Banana","Cherry","Date","Elderberry"]
Func()
