def array_union(first,second):
	try:
		result = []
		if first != []:
			for number in first:
				bull = contains(number,second)
				if bull == True:
					delete_element(first,number)
				else:
					number = int(number)
					result.append(number)
		if second != []:
			for number in second:
					number = int(number)
					result.append(number)
		return result
	except ValueError:
		if number in first:
			delete_element(first,number)
		elif number in second:
			delete_element(second,number)
		return []
def delete_element(array,element):
	array.remove(element)
	return array

def contains(number,second):
	if number in second:
		return True
	else:
		return False
result = []
first = (input("Enter numbers:")).split(",")
second = (input("Enter numbers:")).split(",")
while result == []:
	result = array_union(first,second)
if result != []:
	print(sorted(result))
