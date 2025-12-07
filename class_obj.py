class car:
    color = "red"
    model = "sedan"
    year = 2020


my_car1 = car()
print(my_car1.color) 
print(my_car1.model) 
print(my_car1.year) 


#use class in method
class bike:
    origin = "Japan"
    def __init__(self, name, type):
        self.name = name
        self.type = type

my_bike1 = bike("Yamaha", "Sport")
print(my_bike1.name, my_bike1.type, my_bike1.origin)

my_bike2 = bike("Honda", "Cruiser")
print(my_bike2.name, my_bike2.type, my_bike2.origin)

#practice question using class and method
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum/3

student1 = student("Ammar", [99, 97, 98])
print(student1.name, student1.avg_marks())
