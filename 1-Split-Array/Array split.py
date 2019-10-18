def splitArray(array, arrayType):
	positive = []
	negative = []
	try :
		for element in array:
			element = int(element)
			if element >= 0:
				positive.append(element)
			elif element < 0:
				negative.append(element)
		if arrayType == "+":
			return positive
		else:
			return negative
	except ValueError:
		array.remove(element)
		return String
positive = []
negative = []
error = 0
String = 0
bull = True
array = (input("Enter numbers:")).split(",")
positive = splitArray(array, "+")	
negative = splitArray(array, "-")
while positive == String:
        positive = splitArray(array, "+")
        negative = splitArray(array, "-")
        
while bull:
	if positive != []:
		print(len(positive))
		print(sorted(positive))
	if negative != []:
		print(len(negative))
		print(sorted(negative))
	bull = False
		
