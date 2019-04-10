'''
Question 1 : 
Given an integer array, sort the array according to the frequency of elements in
decreasing order, if frequency of two elements are same then sort in increasing
order.

example 1 :
Input: [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
Output: 3 3 3 3 2 2 2 12 12 4 5

example 2 :
Input: [4, 4, 2, 2, 2, 2, 3, 3, 1, 1, 6, 7, 5]
Output: 2 2 2 2 1 1 3 3 4 4 5 6 7

'''

def swap(i, j):
   arr[i], arr[j] = arr[j], arr[i]

arr = [2,3,2,4,5,12,2,3,3,3,12]
swapped = True
while swapped:
    #This function runs untill all the elements are in the perfect positions.
    swapped = False
    for i in range(1, len(arr)):
        if arr.count(arr[i - 1]) < arr.count(arr[i]):
            swap(i-1,i)
            swapped = True

print(arr)
