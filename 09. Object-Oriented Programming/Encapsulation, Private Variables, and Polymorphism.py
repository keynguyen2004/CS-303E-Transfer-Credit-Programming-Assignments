"""
Encapsulation describes the idea of wrapping data and the methods 
that work on data within one unit. This can

    1. Restricts access to variables and methods directly
    2. Prevents accidental modifications of data

Polymorphism means having many forms. In programming, polymorphism 
means the same function name (but different signatures) being used 
for different types.


Assignments: 

    1. Exercise #1: Private members of the parent class
    2. Exercise #2: Class methods vs. Functions and objects
    3. Exercise #3: Animal - Method overriding
"""

# Exercise #1: Private members of the parent class


# Private instance variable
class Parent(object):
    def __init__ (self):
        self.a = 1
        self.__b = 2     # Notice the double underscore

class Child(Parent):
    def __init__(self):
        self.c = 3
        
        Parent.__init__(self)
if __name__ == "__main__":  
    object = Child()
    print(object.a)
    print(object.b)


# Private method
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)     # This automatically called the update() method,
								    # which append item in iterable into items_list
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update               # private copy of original update() method. Without 
									# this, the update() method called when instantiating        
                                    # the object m will be the update() method of the 
									# MappingSubclass

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
m = MappingSubclass([1,2,3,4])
print(m.items_list)
print(m.update(["one","two","three"], ["these", "are", "values"]))
print(m.items_list)



# Exercise #2: Class methods vs. Functions and objects


# Polymorphism with class methods
class Alice:
	def name(self):
		print("My name is Alice")
	def age(self):
		print("I'm 14 years old")
class Bob:
	def name(self):
		print("My name is Bob")
	def age(self):
		print("I'm 16 years old")

if __name__ == "__main__":
    object1 = Alice()
    object2 = Bob()

    for person in (object1, object2):
        person.name()
        person.age()

# Polymorphism with functions and objects
class Alice:
	def name(self):
		print("My name is Alice")
	def age(self):
		print("I'm 14 years old")
class Bob:
	def name(self):
		print("My name is Bob")
	def age(self):
		print("I'm 16 years old")
		
def DisplayInfo(object):
    object.name()
    object.age()

if __name__ == "__main__":
    object1 = Alice()
    object2 = Bob()

    DisplayInfo(object1)
    DisplayInfo(object2)




# Exercise #3: Animal - Method overriding


class Animal:
    def AnimalSound(self):
        print("Animals make sounds")
        
class Dog:
    def AnimalSound(self):
        print("The dog says woof woof")

class Pig:
    def AnimalSound(self):
        print("The pig says oink oink")
        
if __name__ == "__main__":
    # In inheritance, the child class inherits the 
    # methods from the parent class. However, the 
    # child class can modify the method that it has 
    # inherited from the parent class
    animal = Animal()
    dog = Dog()
    pig = Pig()

    animal.AnimalSound()
    dog.AnimalSound()
    pig.AnimalSound()