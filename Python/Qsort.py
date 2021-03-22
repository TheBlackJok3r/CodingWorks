from random import randint

n = 3
A = []


def RandTab():
    for _ in range(n):
        A.append(randint(0, 10))


def QSort(A=[], start=0, end=n-1):
    if end - start <2:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
    else:
        Starts = start
        EndS = end
        pivot = (start + end) // 2
        print(pivot)
        print(start, end)
        spiv = A[pivot]
        while start < end+1:
            print(start, end)
            if A[start] <= spiv:
                start += 1
            if A[end] > spiv:
                end -= 1
            if A[end] <= spiv and A[start] > spiv:
                A[start], A[end] = A[end], A[start]
                if start > pivot:
                    pivot = start
                elif end < pivot:
                    pivot = end

        QSort(A, Starts, pivot)
        QSort(A, pivot, EndS)


RandTab()
print(A)
QSort(A)
print(A)
