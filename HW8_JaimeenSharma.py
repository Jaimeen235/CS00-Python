'''
Jaimeen Sharma
CS 100 2020F 033
HW 8, Octomber 26, 2020.

'''

# Question 1:

def twoWords(length, firstLetter):
    while True:
        oneWord = input('Enter a '+ str(length)+'-letter word please: ')
        if length == len(oneWord):
            break
    while True:
       twoWord = input('Enter A word beginning with ' + firstLetter+ ' please: ')
       if twoWord[0] == firstLetter.upper() or twoWord[0] == firstLetter.lower():
           break

    return [oneWord,twoWord]

print(twoWords(4,'B'))


# Question 2:

def twoWordsV2(length, firstLetter):
    oneWord = ''
    
    while int(length) != len(oneWord):
        oneWord = input('Enter a '+ str(length)+'-letter word please: ')

    twoWord = ''  
   
    while twoWord[0] != firstLetter:
        twoWord = input('Enter A word beginning with ' + firstLetter + ' please: ')  
       

    return [oneWord,twoWord]

print(twoWordsV2(4,'B'))

# Question 3

def enterNewPassword():

    while True:   
        inputStr = input("Enter password: ")
                        
        if 15 < len(inputStr) < 8 or sum(str.isdigit(c) for c in inputStr) < 1:
            print("Password  required minimum 8 characters ")
            continue
        else:
            print("The password is valid.")
            break

enterNewPassword()

# Question 4

import random
def GuessNumber():
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    number = random.randint(1, 50)
    countValue = 1
    print("Guess", countValue,end="")
    userToguess = int(input("? "))
    while number != userToguess:
        if (countValue == 5 or userToguess == number):
           print("Sorry you have used all tries..the correct number is ", number)     
           break;
        if userToguess < number:
            print(userToguess,"is too low")
            countValue = countValue + 1
            print("Guess", countValue,end="")
            userToguess = int(input("? "))
        elif userToguess > number:
            print(userToguess,"is too high")
            countValue = countValue + 1
            print("Guess", countValue,end ="")
            userToguess = int(input("? "))
        else:
            print ("you are right! I was thinking of ", userToguess,"!")
            break

GuessNumber()












