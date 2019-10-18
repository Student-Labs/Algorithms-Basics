<<<<<<< Updated upstream
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
=======
array = (input("Enter numbers:")).split(",")
positive = []
negative = []
error = 0
def splitArray(array, arrayType):

	while error == 0:
		print(error)
		positive = []
		negative = []
		try :
			for element in array:
				element = int(element)
				if element >= 0:
					positive.append(element)
				if element < 0:
					negative.append(element)
		except ValueError:
			print("Something went wrong.")
			return error == 1
>>>>>>> Stashed changes
		if arrayType == "+":
			return positive
		else:
			return negative
<<<<<<< Updated upstream
			
	except ValueError:
		return error
positive = []
negative = []
error = 0
bull = True
array = (input("Enter numbers:")).split(",")
positive = splitArray(array, "+")
negative = splitArray(array, "-")
while bull:
	if positive != error:
		if negative != error:
				print(len(positive))
				print(sorted(positive))
				print(len(negative))
				print(sorted(negative))
				bull = False
	else :
		choice = input("Could not convert data to an integer.Try again?\nY/N:")
		if choice  == "Y":
			array = (input("Enter numbers:")).split(",")
			positive = splitArray(array, "+")
			negative = splitArray(array, "-")
		if choice == "N":
			break

=======
if error != 1:
        positive = splitArray(array, "+")
        negative = splitArray(array, "-")
        print(len(positive))
        print(positive)
        print(len(negative))
        print(negative)
>>>>>>> Stashed changes
		
