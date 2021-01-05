'''
Jaimeen Sharma
CS 100 2020f Section 033
HW 02, September 11, 2020
'''
print("\n-:Question 1:-\n")

letters  = ['K','G','H','H','H','K','G','H','K','J']
print(letters)
frequency   = [letters.count('G'),letters.count('H'),letters.count('I'),letters.count('J'),letters.count('K')]
print("The letters frequency in a list is: ",frequency)

print("\n-:Question 2:-\n")

"""
a.  Write a Python statement that creates a list named dog_breeds
    that contains the elements 'collie', 'sheepdog', 'Chow', and 'Chihuahua'
    in the order given. 
"""

dogBreeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
print("A Answer is: ", dogBreeds)

"""
b.  Write a Python statement that uses list slicing
    to create a list herding_dogs that is made up of the
    first two elements of dog_breeds.
"""
hredingDogs = (dogBreeds[:2])
print("B Answer is: ", hredingDogs)

"""
c.  Write a Python statement that uses list indexing
    to create a list tiny_dogs that is made up of
    the last element of dog_breeds.
"""

tinyDogs = [dogBreeds[-1]]
print("C Answer is: ", tinyDogs)

"""
d.  Write a Python statement that tests whether
    'Persian' is in the list dog_breeds and prints
    either True or False depending on the answer.
"""

checkBreed = 'Persian' in dogBreeds
print("D Answer is: ", checkBreed)


