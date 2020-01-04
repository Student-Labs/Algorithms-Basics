def printSymbols(columns, type, alphabetRangeStart, alphabetRangeEnd):
    counter = 0
    result = ''
    cyrillicMaxNumber = 64
    latinMaxNumber = 52
    latinNumber = 6
    latinAlphabetRange = range(91, 117)
    for number in range(alphabetRangeStart - 1, alphabetRangeEnd):
        if type != 'all':
            if number in latinAlphabetRange:
                number += latinNumber
            digit = chr(number)
            result = result + digit + ' '
            counter += 1
            if counter % columns == 0:
                result += '\n'
            if type == 'latin':
                if counter == latinMaxNumber:
                    break
            elif type == 'cyrillic':
                if counter == cyrillicMaxNumber:
                    break
        else:
            digit = chr(number)
            result = result + digit + ' '
            counter += 1
            if counter % columns == 0:
                result += '\n'
    print(str(result))


print("""Choose ASCII symbols and press enter:
 1 - All, 2 - Latin, 3 - Cyrillic.""")
type = int(input())
if type == 1:
    type = 'all'
elif type == 2:
    type = 'latin'
elif type == 3:
    type = 'cyrillic'
print("Choose range")
alphabetRangeStart = int(input("From\n"))
alphabetRangeEnd = int(input("To\n"))
cyrillicAlphabetNumber = 1040
latinAlphabetNumber = 65
if type == 'cyrillic':
    alphabetRangeStart = alphabetRangeStart + cyrillicAlphabetNumber
    alphabetRangeEnd = alphabetRangeEnd + cyrillicAlphabetNumber
elif type == 'latin':
    alphabetRangeStart = alphabetRangeStart + latinAlphabetNumber
    alphabetRangeEnd = alphabetRangeEnd + latinAlphabetNumber
columns = int(input("Enter numbers of columns:"))
printSymbols(columns, type, alphabetRangeStart, alphabetRangeEnd)
