'''
Jaimeen Sharma
CS 100 2020F Section 033
HW 5, September 24, 2020
'''

# Question 1

months = ['January','Febuary','March','April',
          'May','June','July','August',
          'September','Octomber','November','December']

for month in months:
    if month[0] == 'J':
        print(month)

# Qquestion 2

for i in range(100):
    if i % 2 == 0 and i % 5 == 0:
        print(i)
     
# Question 3

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter,end =' ')
        
