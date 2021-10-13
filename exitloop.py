#this is an attempt to code bubble sort in python, the goal is to implement a working bubble sort
#then check whether my designed escape works with the scope manipulation I am trying.
import numpy as np

#Standard Bubble Sort
def bblSort(A):
    print("bb start")
    for i in range(len(A) - 2): #-1 or -2?
        for x in range(len(A) - 2 - i):
            if A[x + 1] < A[x]:
               swap(A, x + 1, x)
    print("bb end")
    return A


#Swap Function
def swap(A, pos1, pos2):
    A[pos1], A[pos2]  = A[pos2], A[pos1]
    return A

A = [2 , 8 , 5, 3, 9, 4 , 1]
print("Before sort.")

#pre-sort print
for x in A:
    print(x)

print("sorting:")
bblSort(A)

print("sorted, printing updated list:")
for x in A:
    print(x)
