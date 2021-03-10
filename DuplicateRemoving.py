from random import random
from random import randint

n=1000
A=[]

def RandTab():
    for _ in range(n):
        A.append(randint(0,100))

def BubbleSort(l):
    last=l-2
    first=0
    lasttemp=0
    d=1
    for _ in range(l):
        j=first
        while j!=last+d:
            if A[j]>A[j+1]:
                A[j:j+2]=[A[j+1],A[j]]
                lasttemp=j
            j+=d
        if first==lasttemp:
            break
        last=lasttemp
        d*=-1
        first,last=last,first

def RemoveDuplicates():
    i=0
    k=0
    B=[]
    while i<n-k:
        j=i+1
        while j<n-k:
            if A[i]==A[j]:
                A.remove(A[j])
                k+=1
                j=i+1
            j+=1
        i+=1


RandTab()
print(A)
RemoveDuplicates()
print(A)
BubbleSort(len(A))
print(A)