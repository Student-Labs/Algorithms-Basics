import random
import time
import os

def read_from_file(path):
    numbers = []
    try:
        file = open(path,'r')
        file = file.read()
        file = file.split(",")
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
    except PermissionError:
        print("Something went wrong.")
        return ["Incorrect path"]
    except OSError:
        print("Something went wrong.")
        return["Incorrect path"]
def write_to_file(array,path):
    if array != []:
        file = os.path.basename(path)
        if array == ascending_sorted_array:
                file = "Sorted "+ file
                file = open((file),"tw")
                file.write(str(array))
                file.close()
        elif array == desending_sorted_array:
                fileName = "Reversed sorted " + fileName 
                file = open((fileName),"tw")
                file.write(str(array))
                file.close()

def convert_to_int(text):
    if text == []:
        return text 
    intArray = []
    for symbol in text:
        if symbol in range(-99999,99999):
            digit = int(symbol)
            intArray.append(digit)
            return  intArray
        else:
            print("Numbers in array are very big")
            return ["Incorrect path"]

def quicksort(numbers, direction):
    if len(array) <= 1:
        return array
    else:
        randomNumber = random.choice(array)
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

numbers = []
path = input("Enter path to the file:")
numbers = read_from_file(path)
choice = 0
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
            ascendingSortedArray = quicksort(numbers,"asc")
            desendingSortedArray = quicksort(numbers,"des")
            write_to_file(ascendingSortedArray, path)
            write_to_file(desendingSortedArray, path)
            print(str(time.process_time())+" Seconds")
            print (ascendingSortedArray)
            print(desendingSortedArray)

