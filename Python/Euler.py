def l(highestNum, A):
	#creates list to cover all postions in graph
	for _ in range(highestNum+1):
		A.append([])
	return A

def data(text, A):
	#Appends data on proper positions
	for i in text:
		try:
			x = i.split('.')
			for j in x[1].split(','):
				if not int(j) in A[int(x[0])]:
					A[int(x[0])].append(int(j))
		except:
			pass
	return A

def findBiggest(A, paths):
	#finds biggest index vertex
	num = 0
	for i in range(len(paths)):
		if len(A[paths[i]]) > num:
			num=i
	return num

def emptyTab(A):
	#checks if every position in list is empty
	is_empty = True
	for i in range(len(A)):
		if len(A[i]) != 0:
			is_empty = False
			break
	return is_empty

def findOdd(A):
	#finds odd starting position, in case there isn't one, it returns postion first position with any path
	ret = 0
	for j in range(len(A)):
		if A[j] != []:
			ret=j
			break

	for i in range(len(A)):
		if len(A[i]) % 2 != 0 and len(A[i]) > ret:
			ret = i
	return ret
		

def path(A, start=None, B=[]):
	#returns valid Euler's cycle path, or gives information if there isn't one
	if start == None:
		start = findOdd(A)


	if emptyTab(A) == True:
		return B
	try:
		position = findBiggest(A, A[start])
		s=A[start][position]
		B.append(str(start) + '->' + str(A[start][position]))
		A[A[start][position]].remove(start)
		A[start].remove(A[start][position])
		path(A, s, B)
	except:
		return "This graph isn't Euler's cycle"

	if emptyTab(A) == True:
		return f"This is Euler's cycle and the path is: {B}"
	else:
		return "This graph isn't Euler's cycle"


def Euler():
	A=[]
	highestNum=0
	with open('Euler.txt') as file:
		text = file.read().split(' ')
		for i in text:
			x = int(i.split('.')[0])
			if x>highestNum:
				highestNum=x

		A=l(highestNum, A)
		A=data(text, A)

		return path(A)

print(Euler())