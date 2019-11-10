class numbers:
	def __init__(self,positive,negative):
		self.positive = positive
		self.negative = negative
def split(input):
	try:
		for number in input:
			number = int(number)
			if number < 0:
				if number not in negative:
					negative.append(number)
			else:
				if number not in positive:
					positive.append(number)
		return numbers(positive,negative)
	except ValueError:
		print(str(number) + " is not integer.")
		input.remove(number)
		return split(input)
positive = []
negative = []
input = input("Enter numbers:").split(",")
input = split(input)
if positive != []:
	print(len(positive))
	print(sorted(input.positive))
if negative != []:
	print(len(negative))
	print(sorted(input.negative))
