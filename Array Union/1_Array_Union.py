def array_union(first,second):
	try:
		result = []
		for number in first:
			if number not in second:
				number = int(number)
				result.append(number)
		for number in second:
				number = int(number)
				result.append(number)
		return result
	except ValueError:
		print("Something went wrong.")
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
