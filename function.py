def great():
    print("hello Ammar")

great()

def greet(name):
    print(f"hello {name}")

greet("Ammar")
greet("Ali")
greet("Omar")


def add(a, b):
    return a + b
result = add(5, 3)
print(result)

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
    
print(check_age(20))

def save_2_number(a, b):
    return a + b

print(save_2_number(5, 10))

def name_return(name):
    return name

print(name_return("Ammar"))

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
even_odd_result = even_odd(9)
print(even_odd_result)

def table(num):
    result = ""
    for i in range(1, 10):
        result += f"{num} x {i} = {num * i}\n"
    return result
print(table(5))

def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(10, 20))


# default value
def greet(name="Guest"):
    print(f"hello, {name}!")

greet()
greet("Ammar")

#simple algorithm
def list_sum(number):
    total = 0
    for num in number:
        total += num
    return total

print(list_sum([1, 2, 3, 4, 5]))  # Output: 15

# maximum number in a list
def find_maximum(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

print(find_maximum([3, 5, 2, 8, 1]))  # Output: 8


# simple example in function
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def ammar(function):
    def wrapper():
        print("Ammar Anwer")
        function()
    return wrapper

@ammar
def great():
    print("Hello World")

great()


def my_dec(fun):
    def wrapper():
        print("Start")
        fun()
        print("End")
    return wrapper
@my_dec
def display():
    print("Displaying content")

display()