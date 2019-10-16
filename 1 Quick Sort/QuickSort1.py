import random
import time
import os

def readArrayFromFile(path):
    numbers = []
    try:
        file = open(path,'r')
        file = file.read()
        file = file.split(",")
        print(file)
        print (file)
        text = ""
        for line in file:
            text = text + line
        numbers = toIntArray(text.split())
        if len(numbers) == 0: 
            return[]   
        return numbers 
    except FileNotFoundError:
        print("File does not exist")
        return["Incorrect path"]
    except ValueError:
        print("Could not convert data to an integer")
        return ["Incorrect path"]
def saveSortedArr(array, path):
    if array != []:
        fileName = os.path.basename(path)
        if array == ascendingSortedArray:
                fileName = reverseFileName(fileName)
                file = open((fileName+".py"),"tw")
                file.write(str(array))
                file.close()
        elif array == desendingSortedArray:
                fileName = "Sorted " + fileName + ".py"
                file = open((fileName),"tw")
                file.write(str(array))
                file.close()

def reverseFileName(string):
        invertedString = ""
        length = len(string)
        for index in range(3, length):
                invertedString = invertedString + string[length-index-1]
        return invertedString

def toIntArray(array):
    intArray = []
    for symbol in array:
        digit = int(symbol)
        intArray.append(digit)
    return  intArray

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
    choice = input("Incorrect path.Try again?\nY/N:")
    if choice == "N":
        break
    elif choice == "Y":
        path = input("Enter path to the file:")
        numbers = readArrayFromFile(path)
if choice != "N":
    if numbers != []:
        ascendingSortedArray = quicksort(numbers,"asc")
        desendingSortedArray = quicksort(numbers,"des")
        saveSortedArr(ascendingSortedArray, path)
        saveSortedArr(desendingSortedArray, path)
        print(str(time.process_time())+" Seconds")
        print (ascendingSortedArray)
        print(desendingSortedArray)
if numbers == []:
    print("File is empty")
