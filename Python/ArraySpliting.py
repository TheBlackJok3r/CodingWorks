from random import random
from random import randint

n=100
A=[]

def RandTab():
    for _ in range(n):
        A.append(randint(0,10))

def Split(A, start=0, end=n-1):
    pivot=randint(start,end)
    spiv=A[pivot]
    print(pivot)
    print(A[pivot])
    i=0
    while start<end:
        if A[start]<=spiv:
            start+=1
        if A[end]>spiv:
            end-=1
        if A[end]<=spiv and A[start]>spiv:
            A[start],A[end]=A[end],A[start]
            if start>pivot:
                pivot=start
            elif end<pivot:
                pivot=end

RandTab()
print(A)
Split(A)
print(A)
