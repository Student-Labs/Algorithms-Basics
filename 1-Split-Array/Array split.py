class numbers:
	def __init__(self,positive,negative):
		self.positive = positive
		self.negative = negative
def split(input):
	try:
		for number in input:
			number = int(number)
			if number < 0:
				negative.append(number)
			else:
				positive.append(number)
		return numbers(positive,negative)
	except ValueError:
		input.remove(number)
		return numbers(positive,negative)
positive = []
negative = []
input = (input("Enter numbers:")).split(",")
input = split(input)
if positive != []:
	print(len(positive))
	print(sorted(input.positive))
if negative != []:
	print(len(negative))
	print(sorted(input.negative))
