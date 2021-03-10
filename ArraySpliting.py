from random import random
from random import randint

n=100
A=[]

def RandTab():
    for _ in range(n):
        A.append(randint(0,1000))

def Split(A):
    start=0
    end=n-1
    pivot=A[randint(start,end)]
    print(pivot)
    i=0
    while start<end:
        print(start,end)
        if A[start]<=pivot:
            start+=1
        if A[end]>pivot:
            end-=1
        if A[end]<=pivot and A[start]>pivot:
            A[start],A[end]=A[end],A[start]

RandTab()
print(A)
Split(A)
print(A)
