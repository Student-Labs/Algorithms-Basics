array = (input("Введите числа:")).split(",")
positive = []
negative = []
for element in array:
	try:
		if int(element) < 0:
			negative.append(element)
		else:
			positive.append(element)
		error = 0
	except ValueError:
		print("ValueError")
		error = 1
if error != 1:
	print(len(positive))
	print(positive)
	print(len(negative))
	print(negative)
		
