from random import random
from random import randint

n=100
A=[]

def RandTab():
    for _ in range(n):
        A.append(randint(0,1000))

def Split():
    j=0
    i=0
    global A
    B=[]
    while i!=n:
        if(A[i]<A[j]):
            B.insert(0,A[i])
        else:
            B.append(A[i])
        i+=1
    A=B

RandTab()
print(A)
Split()
print(A)
