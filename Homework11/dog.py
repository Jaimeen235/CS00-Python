'''
Jaimeen Sharma
CS 100, Fall 2020,033
HW 11, November 20, 2020.
'''
    
class Dog:

    ''' Represents dog instances and it's methods '''

    species = 'Canis familiaris'
    
    def __init__(self, name, breed):

        self.name = name
        self.breed = breed
        self.tricks = []
    
    def teach(self,trick):

        self.tricks.append(trick)
        return'{} knows {}'.format(self.name, trick)
    
    def knows(self,trick):

        if trick  == 'frisbee':   
            print('Yes,{} knows {}'.format(self.name, trick))
            return True
        else:
            print('No,{} doesen\'t knows {}'.format(self.name, trick))
            return False
       
   
