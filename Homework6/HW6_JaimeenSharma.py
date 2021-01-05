'''

Jaimeen Sharma
CS 100 2020F Section 033
Homework 6, September 29, 2020.

'''

# Question 1

def hasFinalLetter(strList,letters):
    newList = []
    for letter in strList:
        if letter[-1] in letters:
            newList.append(letter)
    return newList

strList = ['abc','def','ghi']
letters = "afLBfghiPk"

strList2 = ['AbC','GHIj','UdefiY']
letters2 = "GiOlasBpUr"

strList3 = ['AbC','GHIj','Udefi0Y']
letters3 = "nCklxzYtQw"

print(' -: Problem 1 :-')

a = hasFinalLetter(strList,letters)
print(a)

b = hasFinalLetter(strList2,letters2)
print(b)

c = hasFinalLetter(strList3,letters3)
print(c)

# Question 2

def isDivisible(maxInt,twoInts):
    intList = []
    for i in range(1,maxInt):
        if(i % twoInts[0] == 0 and i % twoInts[1] == 0):
            intList.append(i)
    return intList

maxIntCase1 = 7
twoIntsCase1 = (4,9)

maxIntCase2 = 76
twoIntsCase2 = (2,4)

maxIntCase3  = 199
twoIntsCase3 = (3,5)

print('\n','-: Problem 2 :-')

d = isDivisible(maxIntCase1,twoIntsCase1)
print(d)

e = isDivisible(maxIntCase2,twoIntsCase2)
print(e)

f = isDivisible(maxIntCase3,twoIntsCase3)
print(f)
