# 20 Task for Absrtraction
# Abstract Shape class banao jisme area() abstract ho aur Square/Triangle implement karein.
# Animal class banao jo speak() me NotImplementedError raise kare, Dog/Cat override karein.
# Abstract Vehicle class banao jisme start() abstract ho aur stop() normal method ho.
# Serializer Protocol banao jisme serialize(obj) ho aur 2 classes implement karein.
# Abstract BankAccount class banao jisme deposit() & withdraw() abstract ho.
# Formatter abstract class banao jisme format(value) abstract ho aur JSON/CSV implement karein.
# Template Method DataProcessor banao jisme read() & transform() abstract ho.
# Compressor abstract banao aur ZIP/GZIP compressors implement karein.
# StorageBackend abstract banao jisme put() & get() ho aur 2 backends implement karein.
# Plugin abstract banao jisme run() ho aur plugin loader design karo.
# DatabaseFactory abstract banao jisme create_connection() ho aur SQLite/Postgres implement karein.
# PaymentProcessor abstract banao jisme charge() ho aur Stripe/Dummy version banayein.
# ShapeCollection class banao jisme __len__ & __repr__ implement ho.
# CacheProtocol banao jisme get() & set() ho aur 2 cache versions implement karo.
# AsyncFetcher abstract banao jisme async fetch() ho aur dummy async implementation banayein.
# Command abstract banao jisme name & execute() ho aur registry banayein.
# Template Method with hooks banao: before() & after() optional methods implement karo.
# Two abstract classes Flyer & Walker banake Bird implement karo jo dono methods de.
# Storage abstract banao jisme read-only capacity property & used() abstract method ho.
# Versioned PluginBase abstract class banao jisme name, version, run() ho aur loader version check kare.

# t1

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

square = Square(4)
triangle = Triangle(3, 6)
print(f"Square area: {square.area()}")
print(f"Triangle area: {triangle.area()}")

# t2
class Animal(ABC):
    @abstractmethod
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = cat()
print(dog.speak())
print(cat.speak())

# t3
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        return "Vehicle stopped"
class Car(Vehicle):
    def start(self):
        return "Car started"
car = Car()
print(car.start())
print(car.stop())


