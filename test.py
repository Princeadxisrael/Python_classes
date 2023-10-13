#Object Oriented Programming 
#CLASSES are models or blueprints that are used to create objects
##Instantiation is the process of creating instances from a class: An instance is simply an object created from instantiation of a class


#HOW TO DESIGN A CLASS
# Abstraction: Has to do with hiding low level details


# Encapsulation: has to do with keeping methods and properties private inside a class. this means that, the methods
# should not be accessible outside of the clas'

# Inheritance: has to do with a child class inheriting all the methods and properties of the parent class
# The child class can also have methods and properties of their owns


# Polymorphism: describes how child classes are able to modify methods that they inherit from their parent class

# USER{
#     name,
#     email,

#     login(email, password){
#         //logic
#     }
# }

# REGULAR USER{
#         name,
#     email,

#     login(username, email, password){
#         //logic
#     }
# }

# Admin USER{
#         name,
#     email,

#     login(username, key, password){
#         //logic
#     }
# }


# class Cookie:
#     def __init__(self, color):
#         self.color=color

#     def get_color(self):
#         print(self)
#         return self.color

#     def set_color(self, color):
#         self.color=color


# print(Cookie)
# cookie1= Cookie("Red")
# cookie1.set_color("black")
# print(cookie1.get_color())
# print(cookie1)

# cookie2= Cookie("Green")
# cookie2.set_color("indigo")
# print(cookie2.get_color())
# print(cookie2)

# student= { "name": "Chike", "grade": [100,87, 78, 67]}
# def average_grade(sequence):
#     return sum(sequence)/len(sequence)


##create a class that returns a student name and grades and returns the average grade of that particular student

##S.O.L.I.D design and implementation principles that helps us to develop flexible objecte-orientied structures

#S- Single responsibility: a class should have only one reason to change. i.e the class should do one thing and do it very well

# class User:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email

#     def get_name(self):
#         return self.name
    
#     def __str__(self):
#         return f"{self.name} {self.email}"
    
#     def get_email(self):
#         return self.email
    

# user1= User("john", "john@yahoo.com")
# print(user1)

# class Manageuser:
#     def __init__(self):
#            self.users=[]

#     def add_user(self, user):
#         self.users.append(user)

#     def get_users(self):
#         return self.users
    
#     def remove_user(self, user):
#         self.users.remove(user)

# ##O- Open-closed principle: classes or modules should be open 
# ##for modification but closed to extension

# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width=width
#         self.height= height
#     def area(self):
#         return self.width * self.height
    
# class Sqaure(Shape):
#     def __init__(self, width):
#         self.width=width
#     def area(self):
#         return self.width * self.width
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# class AreaCalculator:
#     def __init__(self, shapes):
#         self.shapes=shapes

#     def calculate_area(self):
#         total_area=0
#         for shape in self.shapes:
#             total_area += shape.area()
#         return total_area
    

##L-Liskov substitution Princple states that a child class should be able to be used in plaace of its parent class
##without causing any bugs

# class Vehicle:
#     def start(self):
#         pass
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("car starting")

#     def stop(self):
#         print("car stopping")

# class Bicycle(Vehicle):
#     def start(self):
#         print("Bicycle starting")

#     def stop(self):
#         print("Bicycle stopping")

# def test_vehicle(vehicle):
#     vehicle.start()
#     vehicle.stop()

# car= Car()
# bicycle= Bicycle()

# test_vehicle(car)
# test_vehicle(bicycle)

# ##I-Inteface segregation Princple states that users/clients should not be forced to depend on interfaces or methods that they do not need.

# class Animal:
#     def eat(self):
#         pass

#     def sleep(self):
#         pass

#     def speak(self):
#         pass
#     def fly(self):
#         pass

# # class LivingThing:
# #     def breathe(self):
# #         pass
    
# #     def reproduce(self):
# #         pass

# class Dog(Animal):
#       def eat(self):
#        print("eating")

#       def sleep(self):
#        print("Sleeping")  

#       def speak(self):
#        print("Barking")
#     #   def breathe(self):
#     #         pass
    
#     #   def reproduce(self):
#     #         pass


# class Worm(Dog):
#       def eat(self):
#        print("eating")

#       def sleep(self):
#        print("Sleeping")  

# ##Dependency inversion Princples states that high-levels modules should not depend on low-level modules and vice-versa. 
# # Instead, both high level modules and low level modules should depend on abstractions

# class Database:
#     def save(self, data):
#         pass
#     def load(self):
#         pass

# class User:
#     def __init__(self, database):
#         self.database=database

#     def save(self):
#         data={"name": self.name, "email": self.email}
#         self.database.save(data)

#     def load(self):
#         data=self.database.load()
#         self.name=data["name"]
#         self.email=data['email']

##Class Inheritance
##There are three types of inheritance:
#Single Inheritance- one parent class to a child class
#Multiple Inheritance-- two or more parent to a child class
#Multilevel Inheritance-- a child class inherit another child class


# class Device:
#    def __init__(self, type, connected_by):
#       self.type=type
#       self.connected_by= connected_by
#       self.connected=True
      
#    def __str__(self):
#         return f"Device {self.type} is connected by {self.connected_by}"
   
#    def disconnect(self):
#       self.connected=False
#       print(f"Your {self.type} has been disconnected ")

# class Phone(Device):
#    def __init__(self, type, connected_by, batt_capacity, rom):
#       super().__init__(type, connected_by)
#       self.batt_capacity=batt_capacity
#       self.rom=rom

#    def get_info(self):
#       return f"This {self.type} is connected by {self.connected_by} and has a battery capacity \n of {self.batt_capacity} \n and a rom of {self.rom} "

# class Printer(Device):
#    def __init__(self, type, connected_by, capacity):
#       super().__init__(type, connected_by)
#       self.capacity=capacity
#       self.remaining_pages=capacity

#    def print(self, pages):
#       if not self.connected:
#          return("your device is not connected")
      
#       self.remaining_pages -=pages
#       return f"printing {pages} pages, {self.remaining_pages} pages left"

# class Andriod(Phone):
#    def __init__(self, type, connected_by, batt_capacity, rom):
#       super().__init__(type, connected_by, batt_capacity, rom)

# printer=Printer("Printer", "USB", 500)

# print(printer.print(20))
# print(printer.print(30))

# printer.disconnect()

# print(printer.print(30))

# samsung=Andriod("samsung", "sim", "3400MAH", "3gb")
# print(samsung.get_info())

##  Instance Methods && Variables, Class Methods && Class Variables,, Static Methods and Variable--Class Composition

## If the value of a variable changes from an object to another object, then that variable is called INSTANCE VARIABLE

# class Student:
#     school_name="Moringa School"
#     #constructor
#     def __init__(self, name, reg_num):
#         #instance variables
#         self.name=name
#         self.reg_num=reg_num

#     def show(self):
#         print(f"Name:",{self.name}, "Age: ", {self.reg_num})
#         print(Student.school_name)

# student1=Student("Moses", 21)

# student1.show()

# print(Student.school_name)
##Class Methods and Variables
#- A class variable is a a variable that is declared inside of a class but outside of any instance method or __init__method
#- A class methods are method that are called on the class itself, not on a specific object instance.

from datetime import date

class Student:
    school_name="Moringa School" #class variable
    #constructor
    def __init__(self, name, age):
        #instance variables
        self.name=name
        self.age=age
    @classmethod
    def calc_age(cls, name, birth_year):
        #calc_age take birthyear and returns a new object
        return cls(name, date.today().year - birth_year)
    
    def show(self):
        print(self.name + " 'student age is : " + str(self.age))


esther=Student("Esther", 22)

esther.show()

omotayo=Student.calc_age("Omotayo", 1977)
omotayo.show()