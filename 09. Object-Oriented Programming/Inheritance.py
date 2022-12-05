"""
Types of inheritance

    1. Single inheritance: A child class inherits from only one parent class
    2. Multiple inheritance: A child class inherits from multiple parent classes
    3. Multilevel inheritance: A child class to inherit properties from an immediate 
       parent class which in turn inherits properties from his parent class (i.e. a 
       child and grandchild relationship)
    4. Hierarchical inheritance: More than one child class can inherit properties 
       from a parent class.

Assignments: 

    1. Exercise #1: Petshop
    2. Exercise #2: Student Information
    3. Exercise #3: Painting
"""

# Exercise #1: Petshop
# Single inheritance 

quantity = {}

# In Python (from version 3. x), the object is the root of all classes. 
# In Python 3.x, “class Animal(object)” and “class Animal” are same. 

# Parent class 1
class Animal(object):
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal
     
    def DisplayInfo(self):
        print("My name is", self.name)
        print(self.name, "is a", self.animal)
 
# Child class
class PetShop(Animal):
    def __init__(self, name, animal, species, price):
        self.species = species
        self.price = price
        
        # Invoking the __init__ of the parent class
        Animal.__init__(self, name, animal)
        
    def DisplayDetails(self):
        print("Name:", self.name)
        print("Animal:", self.animal)
        print("Species:", self.species)
        print("Price:", self.price)
    
    def UpdateQuantity(self):
        global quantity
        if self.animal not in quantity:
            quantity[self.animal] = 1
        else:
            quantity[self.animal] += 1
         
    def ReturnQuantity(self):
        print("Number of", self.animal, "available:", quantity[self.animal])

if __name__ == "__main__":   
    Dog1 = PetShop("Alice","Dog","Labrador Retriever",25.99)
    Dog1.DisplayInfo()
    Dog1.UpdateQuantity()
    Dog1.DisplayDetails()
    Dog2 = PetShop("Bob","Dog","German Shepherd",19.99)
    Dog2.UpdateQuantity()
    Dog2.ReturnQuantity()
    Snake1 = PetShop("Toby","Snake","King Cobra",9.99)
    Snake1.UpdateQuantity()
    Snake1.ReturnQuantity()


# Exercise #2: Student Information
# Multiple inheritance

class Student(object):
    def __init__(self, name, StudentID):
        self.name = name
        self.StudentID = StudentID
    
class Grade(object):
    def __init__(self, grade):
        self.grade = grade

class Course(Student,Grade):
    def __init__ (self, name, StudentID, grade, CourseName, CourseID):
        self.CourseName = CourseName
        self.CourseID = CourseID
        
        # Calling constructors of Student and Grade classes
        Student.__init__(self, name, StudentID)
        Grade.__init__(self, grade)
    
    def DisplayStudentInfo(self):
        print("Name:", self.name)
        print("Student ID:", self.StudentID)
    
    def DisplayGrade(self):
        print("Name:", self.name)
        print("Course:", self.CourseName)
        print("Course ID:", self.CourseID)
        print("Grade:", self.grade)

if __name__ == "__main__":   
    Student1 = Course("Alice","s00001",97.5,"Math","Math101")
    Student1.DisplayStudentInfo()


# Exercise #3: Painting
# Multilevel inheritance

class Material(object):
    def __init__(self, canvas, paint, brush = bool):
        self.canvas = canvas
        self.paint = paint
        self.brush = brush
    
    def DisplayMaterial(self):
        print("The materials used involved")
        print("Canvas material:", self.canvas)
        print("Paint used:", self.paint)
        if self.brush == True:
            print("Use brush")
        else:
            print("Use knife or brush alternatives")
        
class Painting(Material):
    # Default arguments must come after the non-default arguments
    # Therefore, brush = bool must be place at the end
    def __init__(self, canvas, paint, name, brush = bool):
        self.name = name
        
        Material.__init__(self, canvas, paint, brush = bool)
        
    def PaintingName(self):
        print("Painting:", self.name)

class Painter(Painting):
    def __init__(self, canvas, paint, name, painter, brush = bool):
        self.painter = painter
        
        Painting.__init__(self, canvas, paint, name, brush = bool)
        
    def PainterName(self):
        print("Painter:", self.painter)

if __name__ == "__main__":
    Painter1 = Painter("Cotton","Oil Painting","Still life","Henry", False)
    Painter1.PainterName(), Painter1.PaintingName(), Painter1.DisplayMaterial()