def print_symbols(columns, type):
	counter = 0
	result = ''
	cyrillicMaxNumber = 64
	latinMaxNumber = 52
	for number in range(alphabetRangeStart-1, alphabetRangeEnd):
		if type == 2:
			if counter == latinMaxNumber:
				break
			if number  not in range(91,97):
				if counter % columns == 0:
					result = result + '\n'
				digit = chr(number)
				result = result + digit + ' '
				counter = counter + 1
		else:
			if type == 3:
				if counter == cyrillicMaxNumber:
					break
			if counter % columns == 0:
				result = result + '\n'
			digit = chr(number)
			result = result + digit + ' '
			counter = counter + 1
	print(str(result))
print("Choose ASCII symbols and press enter: 1 - All, 2 - Latin, 3 - Cyrillic.")
type = int(input())
print("Choose range")
alphabetRangeStart = int(input("From\n"))
alphabetRangeEnd = int(input("To\n"))
cyrillicAlphabetNumber = 1040
latinAlphabetNumber = 65
if type == 3:
	alphabetRangeStart = alphabetRangeStart + cyrillicAlphabetNumber
	alphabetRangeEnd = alphabetRangeEnd + cyrillicAlphabetNumber
elif type == 2:
	alphabetRangeStart = alphabetRangeStart + latinAlphabetNumber
	alphabetRangeEnd = alphabetRangeEnd + latinAlphabetNumber
columns = int(input("Enter numbers of columns:")) 
print_symbols(columns, type)
