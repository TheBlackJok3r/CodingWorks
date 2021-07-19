def data(text, A):
    # Appends data on proper positions
    for i in range(len(text)):
        for j in text[i].split(","):
            if j != '':
                A[i] = A[i] + [int(j)]
    return A


def emptyTab(A):
    # checks if every position in list is empty
    is_empty = True
    for i in range(len(A)):
        if len(A[i]) != 0:
            is_empty = False
            break
    return is_empty


def findBorL(A, paths):
    # finds specific index in given paths
    num = 0
    for i in range(len(paths)):
        if len(A[paths[i]]) > len(A[paths[num]]):
            num = i
    return num


def findAllOdds(A):
    result = []
    for i in range(len(A)):
        if len(A[i]) % 2 != 0:
            result.append(i)
    return result


def findCirc(A, start=None, ret='', d=0):
    if A[start] != []:
        position = findBorL(A, A[start])
        s = A[start][position]
        if ret != '':
            ret += '->' + str(A[start][position])
        else:
            ret += str(start) + '->' + str(A[start][position])
        A[A[start][position]].remove(start)
        A[start].remove(A[start][position])
        result = findCirc(A, s, ret, d+1)
        return result
    return ret


def checkCirc(A, result):
    if emptyTab(A):
        if result[0][0] == result[len(result)-1][len(result[len(result)-1])-1]:
            return [result]
        else:
            return []
    else:
        res = findCirc(A, findBorL(A, [x for x in range(len(A))]))
        if res != '':
            return [result] + [res]
        else:
            return []


def path(A, start=None, ret='', d=0):
    # returns valid Eulerian cycle path, or gives information if there isn't one

    try:
        if(A[start] != []):
            position = findBorL(A, A[start])
            s = A[start][position]
            if ret != '':
                ret += '->' + str(A[start][position])
            else:
                ret += str(start) + '->' + str(A[start][position])
            A[A[start][position]].remove(start)
            A[start].remove(A[start][position])
            return path(A, s, ret, d+1)
    except:
        return "This isn't Eulerian or semi-Eulerian graph"
    return ret


def checkPath(A, res):
    if emptyTab(A):
        if res[0][0] == res[len(res)-1][len(res[len(res)-1])-1]:
            return f"This is Eulerian graph and the curcuit is: {res}"
        else:
            return f"This is semi-Eulerian graph and the path is: {res}"
    else:
        circ = checkCirc(A, findCirc(
            A, findBorL(A, [x for x in range(len(A))])))
        if circ != None:
            for i in circ:
                added = False
                for j in i.split('->'):
                    if added == True:
                        break
                    r = res.split('->')
                    for idx in range(len(r)):
                        if j == r[idx]:
                            res = res[:idx*3]+i+res[idx*3+1:]
                            added = True
                            break
            return checkPath(A, res)
        else:
            return "This isn't Eulerian or semi-Eulerian graph"


def Euler():
    highestNum = 0
    with open('Python/Euler.txt') as file:
        text = file.read().split('\n')
        highestNum = len(text)

        A = [[]] * highestNum
        A = data(text, A)

        odds = findAllOdds(A)
        if odds != []:
            res = path(A, odds[0])
        else:
            res = path(A, findBorL(A, [x for x in range(len(A))]))

        return checkPath(A, res)




