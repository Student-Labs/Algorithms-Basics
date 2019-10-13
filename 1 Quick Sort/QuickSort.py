import random 
numbersArr = []
def readArrayFromFile(arr):
        path = input("Введите путь к файлу:")
        file = open(path)
        text = ""
        for line in file:
            text = text + line
        arr = toIntArray(text.split())
        print(len(arr))
        return arr

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

numbersArr = readArrayFromFile(numbersArr)
sortedArr = quicksort(numbersArr)
print (sortedArr)
