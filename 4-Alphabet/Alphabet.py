def print_simbols(columns,type):
	counter = 0
	result_2 = ''
	for number in range(range_start-1,range_end):
		number = chr(number)+ ' '
		if type == 3:
			if counter == 64:
				break
		elif type == 2:
			if counter in range(26,32):
				number = ''
			if counter == 56:
				break
		if counter % columns == 0:
			result_2 = result_2 + '\n'
		result_2 = result_2 + number 
		counter = counter + 1
	print(str(result_2))
print("Choose ASCII symbols and press enter: 1 - All, 2 - Latin, 3 - Cyrillic. To exit press Ctrl-C.\n")
type = int(input())
print("Choose range")
range_start = int(input("From\n"))
range_end = int(input("To\n"))
if type == 3:
	range_start = range_start + 1040
	range_end = range_end + 1040
elif type == 2:
        range_start = range_start + 65
        range_end = range_end + 65
print(range_start)
print(range_end)
columns = int(input("Enter numbers of columns:")) 
print_simbols(columns,type)
#It`s just a prototype)
