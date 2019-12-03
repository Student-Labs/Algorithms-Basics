def print_simbols(columns):
	counter = 0
	result_2 = ''
	for number in range(range_start,range_end):
		number = chr(number)+ ' '
		if counter % columns == 0:
			result_2 = result_2 + '\n'
		result_2 = result_2 + number 
		counter = counter + 1
	print(str(result_2))
#print("Choose ASCII symbols and press enter: 1 - All, 2 - Latin, 3 - Cyrillic. To exit press Ctrl-C.\n")
#type = int(input())
print("Choose range")
range_start = int(input("From\n"))
range_end = int(input("To\n"))
columns = int(input("Enter numbers of columns:")) 
print_simbols(columns)
#It`s just a prototype)