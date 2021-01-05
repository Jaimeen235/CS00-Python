'''
Jaimeen Sharma
CS 100 2020S Section 106
HW 10, March 31, 2020
'''
      
horton = ['I','Say','What','I','Mean','and','I','Mean','What','I','Say']
d = {}         
def initialLetterCount(horton):
    for elements in horton:
        if elements not in d:
            d[elements[0]] = 1
        else:
            d[elements] += 1
    return d

print(initialLetterCount(horton))

print("\n Problem 2 \n")

def initialLetters(wordList):
    d = {}
    for word in wordList:
        if word not in d:
                d[word[0]] = [word]
    return d


print(initialLetters(horton))

print("\n Problem 3\n")
      
def shareALetter(wordList):
    d = {}
    for word in wordList:
        for letter in word:
            if letter not in d:
                d[letter] = [word]
            else:
                d[letter].append(word)
    return d  

print(shareALetter(horton))







