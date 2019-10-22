class num:
	def __init__(self,positive,negative):
		self.positive = positive
		self.negative = negative
def split(numbers):
	for number in numbers:
		number = int(number)
		if number < 0:
			negative.append(number)
		else:
			positive.append(number)
	return num(positive,negative)
positive = []
negative = []
numbers = (input("Enter numbers:")).split(",")
numbers = split(numbers)
if positive != []:
	print(len(positive))
	print(sorted(numbers.positive))
if negative != []:
	print(len(negative))
	print(sorted(numbers.negative))