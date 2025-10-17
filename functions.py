def great():
    print("Great function executed!")

great()

def myFunction(name):
    print(name + " from myFunction")

myFunction("Hello")
myFunction("How are you?")
myFunction("Goodbye")

def functionArgs(*argd):
    print("type of agruments:", type(argd))
    print("Number 0 agruments:", argd[0])
    print("Number 2 agruments:", argd[2])
    print("ALL agruments:", argd)

# functionArgs(1, 2, 3, 4, 5)
functionArgs("apple", "banana", "cherry")

def my_func():
    x = 300
    print(x)

my_func()