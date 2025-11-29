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