
"""
Jaimeen Sharma
CS 100 Section 033
HW 01, September 10,2020
"""

print("\nExerciese 5b")

month = 8
days = 31
year = 2020

print(month)
print(days)
print(year)
print("\nExerciese 5c")

length_of_pen = 5.5    # length value is in centimeter.
height_of_a_man = 5.72 # height value is in feet and inches.
width_of_a_pole = .30  # width value is in meter.

print(length_of_pen)
print(height_of_a_man)
print(width_of_a_pole)
print("\nExerciese 5d")

month_one = 'January'
course_name = 'Computer Science'
my_fav_movie = 'Harry Potter'

print(month_one)
print(course_name)
print(my_fav_movie)
print("\nBook Exerciese 1.1")

# For the","Hello World!"," program,
print("\nleave out one of","quotation mark cause Syntax Error.")

# leave out both,
print("Invalid Syntax.")

# spell print wrong,
print("Name error:","not defined") 

# 1> what happens if you leave out","one of the parentheses, or both?
print("Answer:","SyntaxError")

"""
2> If you are trying to print a string
what happens if you leave out one of the quotation marks,
or both?

"""
print("Answer:","NameError: name is not defined")

"""
3> You can use a minus sign","to make a negative number like -2.")
What happens if you put a plus")
sign before a number? What about 2++2?")
"""
n = 2++2
print(n)
print("Answer: It will return 4")

"""
4> In math notation,","leading zeros are ok, as in 09.")
What happens if you try this in Python?")
What about 011?")
"""
print("Ansewr:SyntaxError:","invalid token")

#5> What happens if you have","two values with no operator between them?")

print("Aanswer: SyntaxError:","invalid syntax")
print("\n\nBook Exerxiese 1.2")

# 1> How many seconds are there in 42 minutes 42 seconds?")

sec = 1
minute = sec * 60
fortyTwo_Min = minute * 42
fortyTwo_Min = (minute * 42) + (42)

print('\nTotal Seconds are:' , fortyTwo_Min)
 
# 2> How many miles are there in 10 kilometers?")
# Hint: there are 1.61 kilometers in a mile.")

oneMile = 1.6
tenKm = 10/1.6

print('10 Km =',tenKm,'Miles')

"""
3> If you run a 10 kilometer race","in 42 minutes 42 seconds,")
   what is your average pace (time per mile in minutes and seconds)?")
   What is your average speed in miles per hour?")
"""
secTime = fortyTwo_Min / tenKm
timeInMinut = secTime / minute
timeHr = 60 / timeInMinut

print("Average spped in Miles per hour is:", timeHr)
print("\n\nBook Exerciese 2.1")

# We’ve seen that n = 42 is legal. What about 42 = n?")
print("\nAnswer: SyntaxError: can't assign to literal")

#How about x = y = 1?")
print("Answer: It will assign 1 to X and Y variables")

"""
In some languages","every statement ends with a semi-colon, ;.")
What happens if you put a")
semi-colon at the end of a Python statement?")
"""
print("a = 10;")
a = 10;
print(a);

#It will work fine.
#What if you put a period at the end of a statement?")
print("Answer: SyntaxError:","invalid syntax")

"""
In math notation you can multiply x and y like this: xy.")
What happens if you try that in Python?")
"""
print("Answer: NameError: name 'xy' is not defined")
print("\nBook Exerciese 2.2")

"""
1> The volume of a sphere with radius r is 4/3pr3.")
print("What is the volume of a sphere with radius 5?")
"""

radius = 5
pi = 3.14159
sphereVolume = ((4/3) * pi * (radius**3))

print("\nThe volume of sphere", "with radius", radius,"is:",sphereVolume)
"""
2> Suppose the cover price of a book is $24.95,")
but bookstores get a 40% discount.")
Shipping costs $3 for the first copy and 75 cents for each additional copy.")
What is the total wholesale cost for 60 copies?")
"""

book_cover_price = 24.95
bookStore_discount = (book_cover_price *(.40/100)* 100)
shiping_cost = 3
add_copy_cost = .75
pieces = 60
first_copy = ((book_cover_price - bookStore_discount) + (shiping_cost))
remain_copy = ((book_cover_price-bookStore_discount) + (add_copy_cost))
total_Wholesale_Cost = (remain_copy *59)+(first_copy)

print("Wholesale Cost For","60 copis is:",total_Wholesale_Cost)

"""
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
what time do I get home for breakfast?
"""
start_hr = 6+52/60.0
easy_hr = (8+15/60.0)/60.0
tempo_hr = (7+12/60.0)/60.0
running_hr = 2 * easy_hr +3 *tempo_hr
breakfst_hr = start_hr + running_hr
print("Breakfast Hour is:",breakfst_hr)

