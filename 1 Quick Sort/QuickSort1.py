import random
import time
import os

def read_from_file(path):
    numbers = []
    try:
        file = open(path,'r')
        file = file.read()
        file = file.split(',')
        text = ""
        for line in file:
            text = text + line
        numbers = convert_to_int(text.split())
        if numbers == []:
            print("File if empty.")
            return ["Incorrect path"]
        return numbers
    except FileNotFoundError:
        print("File does not exist")
        return["Incorrect path"]
    except ValueError:
        print("Could not convert data to an integer")
        return ["Incorrect path"]
    except Exception:
        print("Something went wrong.")
        return["Incorrect path"]

def convert_to_int(text):
    intArray = []
    if text == []:
        return text
    else:
        for digit in text:
            digit = int(digit)
            if digit in range (-99999,99999):
                intArray.append(digit)
            else:
                print("Numbers in array are very big")
                return ["Incorrect path"]
        return  intArray
        
def quicksort(numbers, direction):
    if len(numbers) <= 1:
        return numbers
    else:
        randomNumber = random.choice(numbers)
        small = []
        big = []
        element = []
        for number in numbers:
            if number < randomNumber:
                small.append(number)
            elif number > randomNumber:
                big.append(number)
            else:
                element.append(number)
        if direction == "asc":
            return quicksort(small, "asc") + element + quicksort(big, "asc")
        else:
            return quicksort(big, "des") + element + quicksort(small, "des")

def write_to_file(array,path):
    if array != []:
        file = os.path.basename(path)
        if array == ascending_sorted_array:
                file = "Sorted "+ file
                file = open((file),"tw")
                file.write(str(array))
                file.close()
        elif array == desending_sorted_array:
                file = "Reversed sorted " + file 
                file = open((file),"tw")
                file.write(str(array))
                file.close()

numbers = []
choice = 0
path = input("Enter path to the file:")
numbers = read_from_file(path)
while numbers == ["Incorrect path"]:
    choice = input("Try again?\nY/N:")
    if choice == "N":
        break
    elif choice == "Y":
        path = input("Enter path to the file:")
        numbers = read_from_file(path)

if choice != "N":
    if numbers != []:
        if numbers != "Incorrect path":
            ascending_sorted_array = quicksort(numbers,"asc")
            desending_sorted_array = quicksort(numbers,"des")
            write_to_file(ascending_sorted_array, path)
            write_to_file(desending_sorted_array, path)
            print(str(time.process_time())+" Seconds")
            print (ascending_sorted_array)
            print(desending_sorted_array)

