import time, timeit
# from addarray import addArray

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
import random

{}

# print (Repeat(testArr))

def calcTime(functiontorun, arrSize, repeat):
    codeToRun = '''
{}(testArr)
'''.format(functiontorun)

    codeToSetup = '''
import time, timeit, random
from random import shuffle
from dupe import Repeat
testArr = random.sample(range(1, 100000), {})
'''.format(arrSize)
    t = timeit.repeat(stmt = codeToRun, setup = codeToSetup, number = 10, repeat = repeat)
    return t

if __name__ == '__main__':
    arrSizes = list(range(500,10000,500))
    # arrSizes = [5, 10, 15, 20, 25, 30, 40, 50]
    # functiontorunstrings = ['testArr.reverse()', 'testArr.sort()', 'shuffle(testArr)', 'testArr[-1]']
    functiontorunstrings = ['Repeat']
    for functionname in functiontorunstrings:
        repetitions = 10
        for size in arrSizes:
            res = calcTime(functionname, size,repetitions)
            sum = 0
            for x in res:
                sum = sum + x
            x = sum / repetitions
            with open("dupe3.csv", "a") as myfile:
                myfile.write("{},     {},     {}\n".format(functionname,size,x))
                myfile.close()
