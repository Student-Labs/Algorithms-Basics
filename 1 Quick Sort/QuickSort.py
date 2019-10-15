import random
import time
import os
numbersArr = []
path = input("Inter path to the file:")

def readArrayFromFile(arr, path):
        file = open(path+".py")
        text = ""
        for line in file:
            text = text + line
        arr = toIntArray(text.split())
        print(len(arr))
        return arr

def makeSortedArr(sortedArr, path):
    fileName = os.path.basename(path)
    reversedFileName = reverseFileName(fileName)
    file = open((reversedFileName+".py"),"tw")
    file.write(str(sortedArr))
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

def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            q = random.choice(arr)
            sArr = []
            mArr = []
            eArr = []
            for n in arr:
                if n < q:
                    sArr.append(n)
                elif n > q:
                    mArr.append(n)
                else:
                    eArr.append(n)
            return quicksort(sArr) + eArr + quicksort(mArr)

numbersArr = readArrayFromFile(numbersArr,path)
sortedArr = quicksort(numbersArr)
sortedArr1 = makeSortedArr(sortedArr,path)
print(str(time.process_time())+" Seconds")
print (sortedArr)
