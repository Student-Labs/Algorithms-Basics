def array_union(first,second):
	try:
		result = []
		if first != []:
			for number in first:
				if number in second:
					first.remove(number)
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
result = []
first = (input("Введите числа:")).split(",")
second = (input("Введите числа:")).split(",")
while result == []:
	result = array_union(first,second)
if result != []:
	print(sorted(result))
