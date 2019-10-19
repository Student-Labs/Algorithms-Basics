def splitArray(array, arrayType):
	positive = []
	negative = []
	try :
		#Так,тут я думаю всё понятно
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
	#Тут тоже объяснений не  требуется
	except ValueError:
		array.remove(element)
		return String
positive = []
negative = []
error = 0
String = 0
array = (input("Enter numbers:")).split(",")
positive = splitArray(array, "+")	
negative = splitArray(array, "-")
#Здесь всё вообще элементарно
while positive == String:
        positive = splitArray(array, "+")
        negative = splitArray(array, "-")
#А тут любой разберётся
if positive != []:
	print(len(positive))
	print(sorted(positive))
if negative != []:
	print(len(negative))
	print(sorted(negative))
		
