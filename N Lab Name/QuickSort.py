numbersArr = [2,5,1,6,4,15,3]
def quicksort(numbersArr):
	randomNumber = random.choice(numbersArr)
	lowArr = []
	nArr = []
	highArr = []
	for n in numbersArr:
		if randomNumber > n :
			n.append(lowArr)
		elif randomNumber < n:
			n.append(highArr)
		else :
			n.append(nArr)
	numbersArr = quicksort(lowArr) + nArr + quicksort(highArr)
	return numbersArr
numbers=quicksort(numbersArr)
print(numbers)
