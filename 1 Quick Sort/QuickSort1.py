import random
import time
import os
numbersArr = []
path = input("Inter path to the file:")

def readArrayFromFile(numbersArr,path):
        file = open(path +".py")
        text = ""
        for line in file:
            text = text + line
        numbersArr = toIntArray(text.split())
        print(len(numbersArr))
        return numbersArr

def makeSortedArr(arr, path):

    fileName = os.path.basename(path)
    reversedFileName = reverseFileName(fileName)
    file = open((fileName+".py"),"tw")
    file.write(str(sortedArr))
    file.close()
        fileName = os.path.basename(path)
        if arr == ("reversedSortedArr "):
                reversedFileName = reverseFileName(fileName)
                open((reversedFileName+".py"),"tw")
                file.write(str(arr))
                file.close()
        elif arr == ("sortedArr"):
                filename = "Sorted "+filename+".py"
                file = open((filename),"tw")
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
        if direction == "+":
            for element in arr:
                if element < randomNum: 
                    sArr.append(element)
                elif element > randomNum:
                    mArr.append(element)
                else:
                    eArr.append(element)
            return quicksort(sArr,"+") + eArr + quicksort(mArr,"+")
        elif direction == "-":
            for element in arr:
                if element<randomNum:
                    mArr.append(element)
                elif element>randomNum:
                    sArr.append(element)
                else :
                    eArr.append(element)
            return quicksort(sArr,"-") + eArr + quicksort(mArr,"-")

numbersArr = readArrayFromFile(path)

ascSortedArr = quicksort(numbersArr,"+")

desSortedArr = quicksort(numbersArr,"-")

sortedArrFile = makeSortedArr(sortedArr, path)

reversedSortedArrFile = makeSortedArr(reversedSortedArr,path)

print(str(time.process_time())+" Seconds")
print (sortedArr)
print(reversedSortedArr)
