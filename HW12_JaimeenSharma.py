'''
Jaimeen Sharma
CS 100 033
HW 12, December 7, 2020.
'''

def safeOpen(fileName):
    try:
        fileOpen = open(fileName)
    except FileNotFoundError:
        return 

inputFile = safeOpen('ghost.txt')
print(inputFile)

def safeFloat(x):
    try:
        a = float(x)
    except ValueError:
        a = float(0)
    return a
    
f = safeFloat('abc')
print(f)


def averageSpeed():
    chance = 1
    while(chance <=2):
        try:
            fileName = open(input("Enter file name : "), "r" )
            lines = fileName.readlines()
            total = 0.0
            carcount = 0
            for line in lines:
                j = line.split(' ')
                for i in j:
                    try:
                        p = safeFloat(i)
                        if p>2:
                            total = total + safeFloat(i)
                            carcount = carcount + 1
                    except ValueError:
                        pass
            print("Average speed is {} miles per hour".format(round(total/carcount,2)))
            break
        except FileNotFoundError:
            if chance == 1:
                print('File not found. Please try again')
            else:
                print('File not found. Yet another human error. Goodbye.')
        chance = chance + 1
averageSpeed()
