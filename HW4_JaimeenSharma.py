'''
Jaimeen Sharma
CS 100 2020F Section 033
HW 04, September 21, 2020
'''
# Question 1

import math

a = 3
b = 4
c = 5

if a < b:
    print("OK")

if c < b:
    print("OK")

if a + b == c:
    print("OK")

if math.sqrt(a**2 + b**2 == c**2):
    print("OK")

# Question 2

if a < b:
    print("OK")
else:
    print("NOT OK")

if c < b:
    print("OK")
else:
    print("NOT OK")

if a + b == c:
    print("ok")
else:
    print("NOT OK")

if math.sqrt(a**2 + b**2 == c**2):
    print("OK")
else:
    print("NOT OK")

# Question 3

for i in range(3):
    clr = input("\nWhat Color: ")
    linWdth = float(input("What Line Width :"))
    linLenth = float(input("What Line Length: "))
    shape = input("line, triangle or square? :")

    import turtle

    screen = turtle.Screen()
    obj = turtle.Turtle()

    angle = 90

    if shape =='line':
        obj.color(clr)
        obj.width(linWdth)
        obj.fd(linLenth)
        
    elif shape == 'triangle':
        obj.color(clr)
        obj.width(linWdth)
        obj.fd(linLenth)
        obj.right(angle + 30)
        obj.fd(linLenth)
        obj.right(angle + 30)
        obj.fd(linLenth)
        
    elif shape == 'square':
        obj.color(clr)
        obj.width(linWdth)
        obj.fd(linLenth)
        obj.right(angle) 
        obj.fd(linLenth)
        obj.right(angle) 
        obj.fd(linLenth)
        obj.right(angle) 
        obj.fd(linLenth)

print('*** Done ***')
         

