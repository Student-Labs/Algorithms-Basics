import random
import time
import os
numbers = []
path = input("Enter path to the file:")

def readArrayFromFile(path):
        file = open(path +".py")
        text = ""
        for line in file:
            text = text + line
        numbers = toIntArray(text.split())
        print(len(numbers))
        return numbers

def makeSortedArr(arr, path):
        fileName = os.path.basename(path)
        reversedFileName = reverseFileName(fileName)
        if arr == (ascendingSortedArr):
                fileName = reverseFileName(fileName)
                file = open((fileName+".py"),"tw")
                file.write(str(arr))
                file.close()
        elif arr == (desendingSortedArr):
                fileName = "Sorted " + fileName + ".py"
                file = open((fileName),"tw")
                file.write(str(arr))
                file.close()

def reverseFileName(string):
        invertedString = ""
        length = len(string)
        for index in range(0, length):
                invertedString = invertedString + string[length-index-1]
        return invertedString

def toIntArray(arr):
    intArr = []
    for symbol in arr:
        digit = int(symbol)
        intArr.append(digit)
    return  intArr


def quicksort(arr, direction):
    if len(arr) <= 1:
        return arr
    else:
        randomNum = random.choice(arr)
        sArr = []
        mArr = []
        eArr = []
        for element in arr:
            if element < randomNum:
                sArr.append(element)
            elif element > randomNum:
                mArr.append(element)
            else:
                eArr.append(element)
        if direction =="+":
            return quicksort(sArr,"+") + eArr + quicksort(mArr,"+")
        else:
            return quicksort(mArr,"-") + eArr + quicksort(sArr,"-")

numbers = readArrayFromFile(path)

ascendingSortedArr = quicksort(numbers,"+")

desendingSortedArr = quicksort(numbers,"-")

ascendingSortedArrFile = makeSortedArr(ascendingSortedArr,path)
desendingSortedArrFile = makeSortedArr(desendingSortedArr,path)

print(str(time.process_time())+" Seconds")
print (ascendingSortedArr)
print(desendingSortedArr)
