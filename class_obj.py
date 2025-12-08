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

class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return f"The {self.brand} {self.model} is starting."
        
    def stop(self):
        return f"The {self.brand} {self.year} is stopping."

mycar1 = car("Toyota","Camry",2021)
print(mycar1.start())
print(mycar1.stop())

class Mobile:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price


    def On(self):
        return f"Calling {self.name} from {self.price}."
    
    def Off(self):
        return f"Turning off {self.name} from {self.brand}."

m1 = Mobile("iPhone","Apple", 1000)
print(m1.On())
print(m1.Off())


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.auther = author
        self.year = year

    def read(self):
        return f"Reading {self.title} by {self.auther}."
    
    def info(self):
        return f"{self.title} was published in {self.year}."
    
b1 = Book("Python Programming","John Doe",2020)
print(b1.read())
print(b1.info())

class Laptop:
    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram

    def boot(self):
        return f"{self.brand} {self.ram} is bootinng up"
    
    def shutdown(self):
        return f"{self.brand} {self.model} is shutting down"
    
L1 = Laptop("Dell","XPS", 16)
print(L1.boot())
print(L1.shutdown())

class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experiance = experience

    def teach(self):
        return f"{self.name} is teaching {self.subject}."
    
    def grade(self):
        return f"{self.name} is grading papers."
    
T1 = Teacher("Ms. Smith","Math", 10)
print(T1.teach())
print(T1.grade())

class BankAccount:
    def __init__(self, acount_number, holder_name, balance):
        self.acount_number = acount_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self):
        return f"Depositing money into account {self.balance}."
    def withdraw(self):
        return f"Withdrawing money from account {self.acount_number}."
    
B1 = BankAccount("123456","Ammar", 5000)
print(B1.deposit())
print(B1.withdraw())

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    def eat(self):
        return f"{self.name} the {self.species} is eating"
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping"
    
A1 = Animal("Dog","Buddy", 3)
print(A1.eat())
print(A1.sleep())

class course:
    def __init__(self, title, instructor, duration):
        self.title = title
        self.instructor = instructor
        self.duration = duration

    def start_course(self):
        return f"The course {self.title} is starting."
    
    def end_course(self):
        return f"The course {self.title} is ending."

C1 = course("Python Basics","Ammar", "4 weeks")
print(C1.start_course())
print(C1.end_course())