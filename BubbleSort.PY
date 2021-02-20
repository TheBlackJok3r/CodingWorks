from random import random
from random import randint

n=100
A=[]


def RandTab():
    for _ in range(100):
        A.append(randint(0,1000))


def BubbleSort1():
    for i in range(n):
        for j in range(n-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]


def BubbleSort2():
    for i in range(n):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]

def BubbleSort3():
    didSwap = False
    for i in range(n):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                didSwap=True
        if didSwap == False:
            break

def BubbleSort4():
    didSwap = False
    last = n-2
    first = 0
    lasttemp=0
    d=1
    for i in range(n):
        j=first
        while j!=last+d:
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                lasttemp=j
                didSwap=True
            j+=d
        if didSwap == False:
            break
        last=lasttemp
        d=d*-1
        first,last = last,first


RandTab()
print(A)
BubbleSort4()
print(A)
