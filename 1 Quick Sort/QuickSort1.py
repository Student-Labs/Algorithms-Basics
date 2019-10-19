import random
import time
import os

def readArrayFromFile(path):
    numbers = []
    try:
        file = open(path,'r')
        file = file.read()
        file = file.split(",")
        text = ""
        for line in file:
            text = text + line
        numbers = toInt(text.split())
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
def saveSortedArr(array, path):
    if array != []:
        fileName = os.path.basename(path)
        if array == ascendingSortedArray:
                fileName = "Sorted "+ fileName
                file = open((fileName),"tw")
                file.write(str(array))
                file.close()
        elif array == desendingSortedArray:
                fileName = "Reversed sorted " + fileName 
                file = open((fileName),"tw")
                file.write(str(array))
                file.close()

def toInt(array):
    if array == []:
        return array 
    intArray = []
    for symbol in array:
        if symbol in range(-99999,99999):
            print (symbol)
            digit = int(symbol)
            intArray.append(digit)
            return  intArray
        else:
            print("Numbers in array are very big")
            return ["Incorrect path"]

def quicksort(array, direction):
    if len(array) <= 1:
        return array
    else:
        randomNumber = random.choice(array)
        s = []
        m = []
        e = []
        for element in array:
            if element < randomNumber:
                s.append(element)
            elif element > randomNumber:
                m.append(element)
            else:
                e.append(element)
        if direction == "asc":
            return quicksort(s, "asc") + e + quicksort(m, "asc")
        else:
            return quicksort(m, "des") + e + quicksort(s, "des")

numbers = []
path = input("Enter path to the file:")
numbers = readArrayFromFile(path)
choice = 0
while numbers == ["Incorrect path"]:
    choice = input("Try again?\nY/N:")
    if choice == "N":
        break
    elif choice == "Y":
        path = input("Enter path to the file:")
        numbers = readArrayFromFile(path)

if choice != "N":
    if numbers != []:
        if numbers != "Incorrect path":
            ascendingSortedArray = quicksort(numbers,"asc")
            desendingSortedArray = quicksort(numbers,"des")
            saveSortedArr(ascendingSortedArray, path)
            saveSortedArr(desendingSortedArray, path)
            print(str(time.process_time())+" Seconds")
            print (ascendingSortedArray)
            print(desendingSortedArray)

