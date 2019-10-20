def split(array, type):
	positive = []
	negative = []
	try :
		for number in array:
			number = int(number)
			if number >= 0:
				positive.append(number)
			elif number < 0:
				negative.append(number)
		if type == "+":
			return positive
		else:
			return negative
	except ValueError:
		print("'"+str(number)+"'" +" is not int.")
		array.remove(number)
		return String
positive = []
negative = []
error = 0
String = 0
array = (input("Enter numbers:")).split(",")
positive = split(array, "+")	
negative = split(array, "-")
while positive == String:
        positive = split(array, "+")
        negative = split(array, "-")
if positive != []:
	print(len(positive))
	print(sorted(positive))
if negative != []:
	print(len(negative))
	print(sorted(negative))
		
