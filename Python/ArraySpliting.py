from random import random
from random import randint

n = 10
A = []


def RandTab():
    for _ in range(n):
        A.append(randint(0, 10))


def Split(A, start=0, end=n-1):
    pivot = randint(start, end)
    spiv = A[pivot]
    print(pivot, spiv)
    i = 0
    while start+1 < end:
        if A[start] <= spiv:
            start += 1
        if A[end] > spiv:
            end -= 1
        if A[end] <= spiv and A[start] > spiv and start < end:
            A[start], A[end] = A[end], A[start]
            if start > pivot:
                pivot = start
            elif end < pivot:
                pivot = end
    return pivot


RandTab()
print(A)
Split(A)
print(A)
