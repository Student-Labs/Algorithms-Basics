import random 
numbersArr = []
def readArrayFromFile(arr):
        file = input("Введите путь к файлу:")
        arr =open(file)
        arr = arr.read()
        arr = arr.split()
        print(len(arr))
        return arr
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
