def Split(A, start, end):
    val = A[start]
    bottom = start + 1
    top = end

    while True:
        while A[top] >= val and top > start:
            top -= 1

        while A[bottom] < val and bottom < end:
            bottom += 1

        if bottom < top:
            A[bottom], A[top] = A[top], A[bottom]
        else:
            break

    A[start], A[top] = A[top], A[start]
    return top


def QSort(A=[], start=0, end=0):
    if start >= end:
        return A
    else:
        pivot = Split(A, start, end)
        QSort(A, pivot+1, end)
        QSort(A, start, pivot-1)


def d(A):
    A = A.split(',')
    for i in range(len(A)):
        A[i] = int(A[i])
    return A


with open('Python/QSortTests.txt') as t:
    tests = t.read().split('\n')
    for i in tests:
        A = d(i)
        QSort(A, 0, len(A)-1)
        print(A)
