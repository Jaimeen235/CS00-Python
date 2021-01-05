
#Jaimeen Sharma
#CS 100 2020F Section 033
#HW 03, September 18, 2020

# Question 1

import turtle
screen = turtle.Screen()

sideLength = 100
wdth = 5

t = turtle.Turtle()

tAngl = 120
t.up()
t.goto(0,0)
t.down()
t.color('orange')
t.width(wdth)
t.fd(sideLength)
t.left(tAngl)
t.fd(sideLength)
t.left(tAngl)
t.fd(sideLength)

sAngl = 90

t.up()
t.right(60)
t.fd(50)
t.down()
t.color('blue')
t.width(wdth)
t.fd(sideLength)
t.right(sAngl)
t.fd(sideLength)
t.right(sAngl)
t.fd(sideLength)
t.right(sAngl)
t.fd(sideLength)

pAngl = 72

t.up()
t.right(90)
t.fd(250)
t.down()
t.color('Yellow')
t.width(wdth)
t.bk(sideLength)
t.left(pAngl)
t.bk(sideLength)
t.left(pAngl)
t.bk(sideLength)
t.left(pAngl)
t.bk(sideLength)
t.left(pAngl)
t.bk(sideLength)

# Question 2

scr = turtle.Turtle()

radius = 50
scr.up()
scr.goto(-50,-260)
scr.left(90)
scr.fd(50)
scr.down()
scr.color('red')
scr.width(wdth)
scr.circle(radius)

radius = 100
scr.up()
scr.right(90)
scr.fd(50)
scr.left(90)
scr.color('light blue')
scr.down()
scr.circle(radius)

radius = 150
scr.up()
scr.right(90)
scr.fd(50)
scr.left(90)
scr.color('green')
scr.down()
scr.circle(radius)

radius = 200
scr.up()
scr.right(90)
scr.fd(50)
scr.left(90)
scr.color('purple')
scr.down()
scr.circle(radius)

# Question 3

import math

a = math.factorial(100)
print('100! =',a)

b = math.log(1000000,2)
print('Log (base 2) of 1,000,000:',b)

c = math.gcd(63,49)
print('The gratest common devicer of 63 and 49 is:',c)
