from random import randint
import random as random
import matplotlib.pyplot as plt

def inPlaceQuickSort(A, start, end):
    if start < end:
        pivot = randint(start, end)
        temp = A[end]
        A[end] = A[pivot]
        A[pivot] = temp

        p = inPlacePartition(A, start, end)
        inPlaceQuickSort(A, start, p - 1)
        inPlaceQuickSort(A, p + 1, end)

        return A


def inPlacePartition(A, start, end):
    pivot = randint(start, end)
    temp = A[end]
    A[end] = A[pivot]
    A[pivot] = temp
    newPivotIndex = start - 1
    for index in xrange(start, end):
        if A[index] < A[end]:  # check if current val is less than pivot value
            newPivotIndex = newPivotIndex + 1
            temp = A[newPivotIndex]
            A[newPivotIndex] = A[index]
            A[index] = temp
    temp = A[newPivotIndex + 1]
    A[newPivotIndex + 1] = A[end]
    A[end] = temp
    return newPivotIndex + 1


X = random.sample(range(1,200), 100)
print "100 random numbers" , X
print "Sorted numbers    ", inPlaceQuickSort(X,0,len(X)-1)



print " "
X = random.sample(range(1,10001), 1000)
print "1000 random numbers" , X
print "Sorted numbers    ", inPlaceQuickSort(X,0,len(X)-1)

print " "
X = random.sample(range(1,100001), 10000)
print "10000 random numbers" , X
print "Sorted numbers    ", inPlaceQuickSort(X,0,len(X)-1)
