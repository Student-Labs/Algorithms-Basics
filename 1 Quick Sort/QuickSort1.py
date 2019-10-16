import random
import time
import os

def readArrayFromFile(path):
    numbers = []
    try:
        file = open(path)
        text = ""
        for line in file:
            text = text + line
        numbers = toIntArray(text.split())
        print(len(numbers))
        return numbers 
    except FileNotFoundError:
        print("File does not exist")
        return[] 
def saveSortedArr(array, path):
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
        for index in range(0, length):
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
        if direction == "+":
            return quicksort(s, "+") + e + quicksort(m, "+")
        else:
            return quicksort(m, "-") + e + quicksort(s, "-")

numbers = []
path = input("Enter path to the file:")
numbers = readArrayFromFile(path)
while numbers == []:
    path = input("Incorrect path.Try again?Y/N:")
    if path == "N":
        break
    elif path == "Y":
        path = input("Enter path:")
        numbers = readArrayFromFile(path)
if path != "N":                                
    ascendingSortedArray = quicksort(numbers,"+")
    desendingSortedArray = quicksort(numbers,"-")
    saveSortedArr(ascendingSortedArray, path)
    saveSortedArr(desendingSortedArray, path)
    print(str(time.process_time())+" Seconds")
    print (ascendingSortedArray)
    print(desendingSortedArray)
