class numbers:
	def __init__(self,positive,negative):
		self.positive = positive
		self.negative = negative
def split(input_numbers):
	try:
		if input_numbers != ['']:
			for number in input_numbers:
				number = int(number)
				if number < 0:
					if number not in negative:
						negative.append(number)
				else:
					if number not in positive:
						positive.append(number)
			return numbers(positive,negative)
		else:
			return []
	except ValueError:
		print(str(number) + " is not integer.")
		input_numbers.remove(number)
		return split(input_numbers)
import random
positive = []
negative = []
input_numbers = input("Enter numbers:").split(",")
input_numbers = split(input_numbers)
while input_numbers == []:
	print("Array is empty.Please try again.")
	input_numbers = input("Enter numbers:").split(",")
	input_numbers = split(input_numbers)
if positive != []:
	print(len(positive))
	print(sorted(input_numbers.positive))
if negative != []:
	print(len(negative))
	print(sorted(input_numbers.negative))
