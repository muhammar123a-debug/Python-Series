# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.age
    
#     def set_age(self, new_age):
#         if new_age >= 0:
#             self.__age = new_age
#         else:
#             print("Age cannot be negative")

# # Without using encapsulation
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = Person("Ali", 20)
# person1.age = -5
# print(f"Person Name: {person1.name}, Age: {person1.age}")

# Encapsulation — Coding Practice (36–50)
# Student class banao → private __age + getter/setter.
# BankAccount class banao → private __balance.
# Withdraw method add karo jisme negative withdraw allow na ho.
# Deposit method add karo jisme negative deposit block ho.
# Car class banao → private __speed + increase/decrease speed.
# User class banao → private __password + verify password method.
# ShoppingCart class → private list __items + add/remove item.
# Employee class → private __salary + increase_salary method.
# Book class → private __price + discount method.
# Customer class → private __phone + setter validation (only digits)
# ProductStock class → private __stock + update stock method.
# Player class → private __health (0–100 only).
# Marks class → marks 0–100 range check in setter.
# Temperature class → private __celsius + convert to Fahrenheit.
# Airport class → private __passengers + add/remove with checks.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age cannot be negative")
# Example usage:
student1 = Student('Ali', 20)
print(student1.get_age())

student1.set_age(25)
print(student1.get_age())

student1.set_age(0)
print(student1.get_age())

# class BankAccount:
#     def __init__(self, initial_balance):
#         self.__balance = initial_balance

#     def withdrow(self, amount):
#         if amount > 0 and amount <= self.initial_balance:
#             self.__balance -= amount
#         else:
#             print("Invalid withdraw amount")
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid deposit amount")
#     def get_balance(self):
#         return self.__balance
    
# # Example usage:
# account = BankAccount(1000)
# print(account.get_balance())
# account.deposit(500)
# print(account.get_balance())
# account.withdrow(10)
# print(account.get_balance())
# account.withdrow(2000)  # Invalid withdraw amount
# account.deposit(-100)   # Invalid deposit amount
# print(account.get_balance())


class Car:
    def __init__(self):
        self.__speed = 0
    
    def increase_speed(self, increment):
        if increment > 0:
            self.__speed += increment
        else:
            print("Increment must be positive")
    def decrease_speed(self, decrement):
        if decrement > 0 and self.__speed - decrement >= 0:
            self.__speed -= decrement
        else:
            print("Decrement must be positive and cannot reduce speed below 0")
    
    def get_spped(self):
        return self.__speed
# Example usage:
car = Car()
print(car.get_spped())
car.increase_speed(50)
print(car.get_spped())

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    
    def verify_password(self, password):
        return self.__password == password
u1 = User("User1","Pass123")
print(u1.verify_password("Pass123"))  # True

print(u1.verify_password("123"))

class ShoppingCart:
    def __init__(self):
        self.__item = []
    
    def add_item(self, item):
        self.__item.append(item)

    def remove_item(self, item):
        if item in self.__item:
            self.__item.remove(item)
        else:
            print("Item not found in cart")
    
    def get_item(self):
        return self.__item

cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
print(cart.get_item())
cart.remove_item("Apple")
print(cart.get_item())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def increae_salary(self, amount):
        if amount >= 0:
            self.__salary += amount
        else:
            print("Increase amount must be non-negative")

    def get_salary(self):
        return self.__salary

emp = Employee("john", 50000)
print(emp.get_salary())
emp.increae_salary(5000)
print(emp.get_salary())


class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price
    def apply_discount(self, dicount):
        self.__price -= dicount
    
    def get_price(self):
        return self.__price
book = Book("Python Programming", 100)
price = book.get_price()
print(price)
book.apply_discount(20)
print(book.get_price())


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.__phone = phone
    def set_phone(self, new_phone):
        if new_phone.isdigit():
            self.__phone = new_phone
        else:
            print("Phone number must contain only digits")
    def get_phone(self):
        return self.__phone

customer1 = Customer("Alice", "1234567890")
print(customer1.get_phone())
customer1.set_phone("9876543210")
print(customer1.get_phone())

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock
    
    def update_stock(self, amount):
        if amount >= 0:
            self.__stock = amount
        else:
            print("Stock cannot be negative")

    def get_stock(self):
        return self.__stock
    
product1 = Product("Laptop", 50)
print(product1.get_stock())
product1.update_stock(30)
print(product1.get_stock())


class Player:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
    
    def set_health(self, new_health):
        if 0 <= new_health <= 100:
            self.__health = new_health
        else:
            print("Health must be between 0 and 100")
    
    def get_health(self):
        return self.__health

player1 = Player("Hero", 80)
print(player1.get_health())
player1.set_health(90)
print(player1.get_health())

class Marks:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
             self.__marks = new_marks
        else:
            print("Marks must be between 0 and 100")
marks1 = Marks("Bob", 87)
print(marks1.get_marks())
marks1.set_marks(90)
print(marks1.get_marks())

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
temp = Temperature(25)
print(temp.to_fahrenheit())


class Airport:
    def __init__(self):
        self.__passengers = 0
    
    def add_passenger(self):
        self.__passengers += 1
    
    def remove_passenger(self):
        if self.__passengers > 0:
            self.__passengers -= 1
        else:
            print("No passengers to remove")
    
    def get_passengers(self):
        return self.__passengers

airport = Airport()
airport.add_passenger()
print(airport.get_passengers())
airport.remove_passenger()
print(airport.get_passengers())
airport.add_passenger()
print(airport.get_passengers())


class Patient:
    def __init__(self, name, age, bed_number, diagnosis):
        self.name = name
        self.__age = age
        self.__bed_number = bed_number
        self.__diagnosis = diagnosis

    def get_age(self):
        if self.__age >= 0:
            return self.__age
        else:
            print("Age cannot be negative")
    
    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative")
    
    def get_bed_number(self):
        return self.__bed_number

    def set_bed_number(self, new_bed_number):
        if new_bed_number >= 0:
            self.__bed_number = new_bed_number
        else:
            print("Bed number cannot be negative")
    
    def get_diagnosis(self):
        return self.__diagnosis

    def set_diagnosis(self, new_diagnosis):
        self.__diagnosis = new_diagnosis

patient1 = Patient("Asim", 30, 101, "Flu")
print(patient1.name,patient1.get_age(),patient1.get_bed_number(), patient1.get_diagnosis())
patient1.__age(15)
print(patient1.get_age())
print(patient1.name,patient1.get_age(),patient1.get_bed_number(), patient1.get_diagnosis())