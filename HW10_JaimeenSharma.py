'''
Jaimeen Sharma
CS 100 2020F 033
HW 10, November 08, 2020.
'''

horton = ['I','say','what','I','mean','and','I','mean','what','I','say']

def initialLetterCount(wordList):
    dictionary = {}
    for words in range(len(wordList)):
        if wordList[words][0] in dictionary.keys():
            dictionary[wordList[words][0]] = dictionary[wordList[words][0]] + 1
        else:
            dictionary[wordList[words][0]] = 1
    return dictionary

print(initialLetterCount(horton))

def initialLetters(wordList):
    dictionary = {}
    for words in wordList:
        if words not in dictionary.keys():
            dictionary[words[0]] = [words]
    return dictionary

print(initialLetters(horton))

def shareOneLetter(wordList):
    dictionary = {}
    for word in wordList:
        if word not in dictionary.keys():
            dictionary[word] = []

    for key in dictionary.keys():
        for char in key:
            for word in wordList:
                if char in word and word not in dictionary[key]:
                    dictionary[key].append(word)
            
    return dictionary

print(shareOneLetter(horton))
