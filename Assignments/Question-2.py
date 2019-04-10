'''
Question 2 : 
Given a string str and an array of strings strArr[], the task is to sort the
array according to the alphabetical order defined by str.
Note: str and every string in strArr[] consists of only lower case alphabets.

Examples:

Input: str = “fguecbdavwyxzhijklmnopqrst”,
strArr = [“game”, “is”, “the”, “best”, “place”, “for”, “learning”]
Output: for game best is learning place the

Input: str = “avdfghiwyxzjkecbmnopqrstul”,
strArr[] = {“rainbow”, “consists”, “of”, “colours”}
Output: consists colours of rainbow
'''
str1 = "fguecbdavwyxzhijklmnopqrst"

strArr = ["game", "is", "the", "best", "place", "for", "learning"]

def swap(i,j):
    strArr[i], strArr[j] = strArr[j], strArr[i]

swapped = True
while swapped:
    swapped = False
    for i in range(1, len(strArr)):
        if str1.index(strArr[i-1][0]) > str1.index(strArr[i][0]):
            swap(i-1,i)
            swapped = True

print(strArr)
