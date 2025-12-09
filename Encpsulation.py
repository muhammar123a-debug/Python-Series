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

# Without using encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Ali", 20)
person1.age = -5
print(f"Person Name: {person1.name}, Age: {person1.age}")