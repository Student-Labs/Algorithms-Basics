def printSymbols(columns, type,alphabetRangeStart,alphabetRangeEnd):
	counter = 0
	result = ''
	cyrillicMaxNumber = 64
	latinMaxNumber = 52
	latinNumber = 6
	latinAlphabetRange = range(91,117)
	for number in range(alphabetRangeStart-1, alphabetRangeEnd):
		if type != 1:
			if number not in latinAlphabetRange:
				digit = chr(number)
				result = result + digit + ' '
				counter += 1
				if counter % columns == 0:
					result += '\n'
			elif number in latinAlphabetRange:
				number += latinNumber
				digit = chr(number)
				result = result + digit + ' '
				counter += 1
				if counter % columns == 0:
					result += '\n'
			if type == 2:
				if counter == latinMaxNumber:
					break
			if type == 3:
				if counter == cyrillicMaxNumber:
					break
		else:
			digit = chr(number)
			result = result + digit + ' '
			counter += 1
			if counter % columns == 0:
				result += '\n'
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
print_symbols(columns, type,alphabetRangeStart,alphabetRangeEnd)
