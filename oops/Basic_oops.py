#class and object in python
#class is like blueprint to the code
#object --> object is used as instance of class

class car:
    #__init__ -->constructor in class
    def __init__(self,name): #self is a reference to the current object.
        self.name=name #--> this referring to the object
    def display(self):
        print(self.name)
s1=car("Avinash") #-->object created in python
s1.display()