# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i+1, len(arr)):
            if (arr[j] < arr[smallest_index]):
                smallest_index = j


        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr

arr = [17,8,12,3,50]
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # for a number in range of len array (start, stop, step)
    # start at end of array, stop at 0th index, step through by 1
    for num in range(len(arr)-1,0,-1):
        # for i in num list
        for i in range(num):
            # if current i is greater than next i
            if arr[i]>arr[i+1]:
                # temporarily assign value
                temp = arr[i]
                # swap index values
                arr[i] = arr[i+1]
                # assign to temp
                arr[i+1] = temp
    return arr

arr = [0,3,2,1,20,10,13,15]
bubble_sort(arr)
print(arr)

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
