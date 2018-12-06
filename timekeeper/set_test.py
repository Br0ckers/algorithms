import time, timeit
# from addarray import addArray

def test_set(x):
    seen = set()
      # O(1) lookups
    for i in x:
        if i not in seen:
            seen.add(i)
        else:
            return i

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
from set_test import test_set
testArr = random.sample(range(1, 100000), {})
'''.format(arrSize)
    t = timeit.repeat(stmt = codeToRun, setup = codeToSetup, number = 10, repeat = repeat)
    return t

if __name__ == '__main__':
    arrSizes = list(range(500,10000,500))
    # arrSizes = [5, 10, 15, 20, 25, 30, 40, 50]
    # functiontorunstrings = ['testArr.reverse()', 'testArr.sort()', 'shuffle(testArr)', 'testArr[-1]']
    functiontorunstrings = ['test_set']
    for functionname in functiontorunstrings:
        repetitions = 10
        for size in arrSizes:
            res = calcTime(functionname, size,repetitions)
            sum = 0
            for x in res:
                sum = sum + x
            x = sum / repetitions
            with open("set_1.csv", "a") as myfile:
                myfile.write("{},     {},     {}\n".format(functionname,size,x))
                myfile.close()
