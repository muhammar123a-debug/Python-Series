# class car:
#     color = "red"
#     model = "sedan"
#     year = 2020


# my_car1 = car()
# print(my_car1.color) 
# print(my_car1.model) 
# print(my_car1.year) 


# #use class in method
# class bike:
#     origin = "Japan"
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

# my_bike1 = bike("Yamaha", "Sport")
# print(my_bike1.name, my_bike1.type, my_bike1.origin)

# my_bike2 = bike("Honda", "Cruiser")
# print(my_bike2.name, my_bike2.type, my_bike2.origin)

# #practice question using class and method
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         return sum/3

# student1 = student("Ammar", [99, 97, 98])
# print(student1.name, student1.avg_marks())


# Step 1: 10 simple classes banao (practice)
# Step 2: Har class mai yeh likho:
# 3–4 attributes
# 2 methods
# Ek object create karo
# Method call karo

# class car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         return f"The {self.brand} {self.model} is starting."
        
#     def stop(self):
#         return f"The {self.brand} {self.year} is stopping."

# mycar1 = car("Toyota","Camry",2021)
# print(mycar1.start())
# print(mycar1.stop())

# class Mobile:
#     def __init__(self, name, brand, price):
#         self.name = name
#         self.brand = brand
#         self.price = price


#     def On(self):
#         return f"Calling {self.name} from {self.price}."
    
#     def Off(self):
#         return f"Turning off {self.name} from {self.brand}."

# m1 = Mobile("iPhone","Apple", 1000)
# print(m1.On())
# print(m1.Off())


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.auther = author
#         self.year = year

#     def read(self):
#         return f"Reading {self.title} by {self.auther}."
    
#     def info(self):
#         return f"{self.title} was published in {self.year}."
    
# b1 = Book("Python Programming","John Doe",2020)
# print(b1.read())
# print(b1.info())

# class Laptop:
#     def __init__(self, brand, model, ram):
#         self.brand = brand
#         self.model = model
#         self.ram = ram

#     def boot(self):
#         return f"{self.brand} {self.ram} is bootinng up"
    
#     def shutdown(self):
#         return f"{self.brand} {self.model} is shutting down"
    
# L1 = Laptop("Dell","XPS", 16)
# print(L1.boot())
# print(L1.shutdown())

# class Teacher:
#     def __init__(self, name, subject, experience):
#         self.name = name
#         self.subject = subject
#         self.experiance = experience

#     def teach(self):
#         return f"{self.name} is teaching {self.subject}."
    
#     def grade(self):
#         return f"{self.name} is grading papers."
    
# T1 = Teacher("Ms. Smith","Math", 10)
# print(T1.teach())
# print(T1.grade())

# class BankAccount:
#     def __init__(self, acount_number, holder_name, balance):
#         self.acount_number = acount_number
#         self.holder_name = holder_name
#         self.balance = balance

#     def deposit(self):
#         return f"Depositing money into account {self.balance}."
#     def withdraw(self):
#         return f"Withdrawing money from account {self.acount_number}."
    
# B1 = BankAccount("123456","Ammar", 5000)
# print(B1.deposit())
# print(B1.withdraw())

# class Animal:
#     def __init__(self, species, name, age):
#         self.species = species
#         self.name = name
#         self.age = age
#     def eat(self):
#         return f"{self.name} the {self.species} is eating"
    
#     def sleep(self):
#         return f"{self.name} the {self.species} is sleeping"
    
# A1 = Animal("Dog","Buddy", 3)
# print(A1.eat())
# print(A1.sleep())

# class course:
#     def __init__(self, title, instructor, duration):
#         self.title = title
#         self.instructor = instructor
#         self.duration = duration

#     def start_course(self):
#         return f"The course {self.title} is starting."
    
#     def end_course(self):
#         return f"The course {self.title} is ending."

# C1 = course("Python Basics","Ammar", "4 weeks")
# print(C1.start_course())
# print(C1.end_course())


# # 10 practice questions 
# Student class banao → name, age attributes + study method.
# Car class banao → brand, model + start_engine method.
# Circle class banao → radius + area method.
# Employee class banao → salary + bonus method.
# Product class banao → price, discount method.
# Dog class banao → bark method jo "Woof!" return kare.
# Rectangle class banao → length, width + calculate area.
# BankCustomer class banao → welcome method.
# Country class banao → population + density method.
# Laptop class banao → RAM, CPU + show_specs method.

# Without using encapsulation
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self):
        return f"{self.name} is studying."

student1 = Student("Ammar", 20)
print(student1.study())

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"The engin of {self.brand}  {self.model} is starting"

car1 = Car("Toyota", "Camry")
print(car1.start_engine())

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
circle1 = Circle(5)
print(f"Area of circle: {circle1.area()}")


class Employee:
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus
    
    def total_compensation(self):
        return self.salary + self.bonus
employee1 = Employee(50000, 5000)
print(f"Total compensation: {employee1.total_compensation()}")


class Product:
    def __init__(self, price, discount):
        self.price = price
        self.dicount = discount

    def discounted_price(self):
        return self.price - (self.price * self.dicount / 100)
    
product1 = Product(1000, 10)
print(f"Dicounted price: {product1.discounted_price()}")

class Dog:
    def bark(self):
        return "woof!"
dog1 = Dog()
print(dog1.bark())

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def calculate_area(self):
        return self.lenght - self.width

rectangle1 = Rectangle(10, 9)
print(rectangle1.calculate_area())

class BankCustomer:
    def welcome(self):
        return "Welcome to the bank!"
    
bank_customer1 = BankCustomer()
print(bank_customer1.welcome())

class Country:
    def __init__(self, population, area):
        self.population = population
        self.area = area
    
    def density(self):
        return self.population / self.area

country1 = Country(1000000, 50000)
print(f"Population density: {country1.density()}")

class Laptop:
    def __init__(self, RAM, CPU):
        self.RAM = RAM
        self.CPU = CPU
    
    def show_spaces(self):
        return f"Laptop specs - RAM: {self.RAM}, CPU: {self.CPU}"

laptop1 = Laptop("16GB", "Intel i7")
print(laptop1.show_spaces())