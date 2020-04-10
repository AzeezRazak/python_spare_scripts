import operator
import random
from random import randint

operators = [('+', operator.add), ('-', operator.sub)]

def random_with_N(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_with_nn(n):
    range_start = 10**(n-1)
    range_end = a
    return randint(range_start, range_end)

x=0
stgNum = 1
lvlNum = int(input("Enter number of questions per level: "))

for x in range(lvlNum):

    a = random_with_N(stgNum)
    b = random_with_nn(stgNum)
    op, fn = random.choice(operators)
    userInput = int(input("{} {} {} = ".format(a, op, b)))
    if userInput == fn(a, b):
        print("Correct")
        x = x+1
    elif userInput != fn(a,b):
        print("Incorrectly")
        x = x

print("Score" + str(x) + "/" + str(lvlNum))
    #print("{} {} {} = {}".format(a, op, b, fn(a, b)))



"""
==========================================================================================
"""


import operator
import random
from random import randint

operators = [('+', operator.add), ('-', operator.sub)]

def random_with_N(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_with_nn(n, a):
    range_start = 10**(n-1)
    range_end = a
    return randint(range_start, range_end)


stgNum = 1

def qn_equation(lvlNum,stgNum,x=0):
    print("Level {}".format(str(stgNum)))
    for xY in range(lvlNum):

        a = random_with_N(stgNum)
        b = random_with_nn(stgNum, a)
        op, fn = random.choice(operators)
        userInput = int(input("{} {} {} = ".format(a, op, b)))

        if userInput != fn(a,b):
            print("Incorrectly")

        elif userInput == fn(a, b):
            print("Correct")
            x=x+1
    global ScoreList
    ScoreList = ["abc"]
    text = "Level " + str(stgNum) + ": " + str(x) + "/" + str(lvlNum)

    ScoreList.append(text)
    join(ScoreList)
    print(ScoreList[stgNum])
    print("Score: " + str(x) + "/" + str(lvlNum))
    #print("{} {} {} = {}".format(a, op, b, fn(a, b)))

Num = int(input("Enter number of questions per level: "))
qn_equation(Num, stgNum)


def score():
    for i in range(1, stgNum):
        print(ScoreList[stgNum])

def loopQuestion(stgNum):
    enter = input("Press Enter to proceed to level {} or Q to Quit: ".format(str(stgNum+1)))
    if enter == '':
        stgNum = stgNum + 1
        qn_equation(Num, stgNum)
        loopQuestion(stgNum)
    elif enter == 'q':
        score()


loopQuestion(stgNum)
