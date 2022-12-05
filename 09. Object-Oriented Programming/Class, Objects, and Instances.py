"""
Object-Oriented Programming 

    - Creates classes
    - … as a blueprint for an object // objects are instances of classes 
    - … that have properties/attributes and methods  
    - … that can be private to the class // properties can only be accessed by the class's methods // encapsulation 

Assignments:

    1. Exercise #1: Class objects
    2. Exercise #2: Instance and Method objects
    3. Exercise #3: The __init__ method
    4. Exercise #4: Class and Instance variables
    5. Exercise #5: Animals and PetShop

"""

# Exercise #1: Class objects


# Attribute references & Instantiation
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):                        # 'self' has no special meaning to Python  
        return 'hello world'            # - it's just convention
         
if __name__ == "__main__": 
    MyClass.i                           # This is a valid attribute reference, 
    MyClass.f                           # This is a valid attribute reference, 
                                        # returning a function object
    MyClass.__doc__                     # Magic method/dunder method,

# Another approach is Instantiation - creating an object
    x = MyClass()                       # Creates a new instance of the class and assigns      
    x.i				                    # object to the local variable
    x.f()
    MyClass.f(x)                        # x.f() is the equivalent of MyClass.f(x)



# Exercise #2: Instance and Method objects

# Instance object
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

if __name__ == "__main__":
    x = MyClass()            # Instantiate MyClass()
    x.counter = 1            # Add a data attribute and assign a value
    x.counter

    while x.counter <= 4:
        x.counter *= 2
        # first loop x.counter == 2
        # second loop x.counter == 4
        # third loop does not start as x.counter > 4

    print(x.counter)
    del x.counter            # Delete the data attribute
    print(x.counter)         # Attribute error

# Method object
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

if __name__ == "__main__":
    x = MyClass()            # Instantiate MyClass()
    x.f()                    # Usually, a method is called right after it is bound
    xf = x.f
    while True:
        print(xf())          # And this will continue to print hello world forever 



# Exercise #3: The __init__ method

class Car:
    # Sometimes it's necessary to specify the data type
    def __init__(self, brand, model, color, price: float):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
   
    def PriceDepreciation(self):
        NewPrice = self.price * 0.9
        print("New price is:", NewPrice)
		
if __name__ == "__main__":
    x = Car("Toyota", "Land Cruiser", "blue", 25_999.95)                                      
    print(x.brand, x.model, x.color, x.price)
    x.PriceDepreciation()


class Animals:
    # Class atributes
    attribute1 = "mammal"
    attribute2 = "bird"
    attribute3 = "fish"
    attribute4 = "reptile"
    attribute5 = "amphibian"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def DisplayInfo(self):
        print("My name is", self.name)
        print("My age is", self.age)

if __name__ == "__main__":
    # Object instantiation
    Dog = Animals("Toby", 3)
    Snake = Animals("Alice", 2)

    # Accessing class attributes
    print("Toby is a", Dog.attribute1)
    print("Alice is a", Snake.attribute4)

    # Accessing instance attributes
    Dog.DisplayInfo()
    Snake.DisplayInfo()



# Exercise #4: Class and Instance variables

class Animals:

    type = "pet"                     # class variable shared by all instances

    # Class atributes
    attribute1 = "mammal"
    attribute2 = "bird"
    attribute3 = "fish"
    attribute4 = "reptile"
    attribute5 = "amphibian"
   
	   # Instance attributes
    def __init__(self, name, age):
        self.name = name             # instance variable unique to each instance
        self.age = age               # instance variable unique to each instance
        self.tricks = []             # instance variable unique to each instance...
    
    def DisplayInfo(self):
        print("My name is", self.name)
        print("My age is", self.age)

    def AddTrick(self,trick):        # We pass a trick as an argument and it appends
        self.tricks.append(trick)    # the trick to the list of the 
                                     # instance variable self.tricks

if __name__ == "__main__":
    # Object instantiation
    Dog = Animals("Toby", 3)
    Snake = Animals("Alice", 2)

    print(Dog.type)                     # The type attribute is shared by all animal

    print(Snake.type)                   # The type attribute is shared by all animal


    # Accessing class attributes
    print("Toby is a", Dog.attribute1)
    print("Alice is a", Snake.attribute4)

    # Accessing instance attributes
    Dog.DisplayInfo()
    Snake.DisplayInfo()

    Dog.AddTrick("Roll over")
    Snake.AddTrick("Traverse a maze")
    print(Dog.tricks)
    print(Snake.tricks)
 



# Exercise #5: Animals and PetShop

class Animals:

    type = "pet"                     # class variable shared by all instances

    # Class atributes
    attribute1 = "mammal"
    attribute2 = "bird"
    attribute3 = "fish"
    attribute4 = "reptile"
    attribute5 = "amphibian"
   
    # Instance attributes
    def __init__(self, name, age):
        self.name = name             # instance variable unique to each instance
        self.age = age               # instance variable unique to each instance
        self.tricks = []             # instance variable unique to each instance

    def DisplayInfo(self):
        print("My name is", self.name)
        print("My age is", self.age)

    def AddTrick(self,trick):        # We pass a trick as an argument and it appends
        self.tricks.append(trick)    # the trick to the list of the 
                                     # instance variable self.tricks

if __name__ == "__main__":
    # Object instantiation
    Dog = Animals("Toby", 3)
    Snake = Animals("Alice", 2)

    print(Dog.type)                     # The type attribute is shared by all animal
    print(Snake.type)                   # The type attribute is shared by all animal


    # Accessing class attributes
    print("Toby is a", Dog.attribute1)
    print("Alice is a", Snake.attribute4)

    # Accessing instance attributes
    Dog.DisplayInfo()
    Snake.DisplayInfo()

    Dog.AddTrick("Roll over")
    Snake.AddTrick("Traverse a maze")
    print(Dog.tricks)
    print(Snake.tricks)
