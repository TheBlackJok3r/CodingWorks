from random import seed
from random import randint

n=100
A=[]
seed(1)


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




RandTab()
print(A)
BubbleSort3()
print(A)
