# def great():
#     print("Great function executed!")

# great()

# def myFunction(name):
#     print(name + " from myFunction")

# myFunction("Hello")
# myFunction("How are you?")
# myFunction("Goodbye")

# def functionArgs(*argd):
#     print("type of agruments:", type(argd))
#     print("Number 0 agruments:", argd[0])
#     print("Number 2 agruments:", argd[2])
#     print("ALL agruments:", argd)

# # functionArgs(1, 2, 3, 4, 5)
# functionArgs("apple", "banana", "cherry")

# def my_func():
#     x = 300
#     print(x)

# my_func()

#LOGIN SYSTEM
#Register
def register(username, password, user_db):
    if username in user_db:
        return "Username alerady exists."
    user_db[username] = password
    return "Registration successful."
#Login
def Login(username, password, user_db):
    if username not in user_db:
        return "Username does not exist."
    if user_db[username] != password:
        return "Incorrect password."
    return "Login successful."

# Example user database
user_db = {}
# Register a new user
print(register("user1", "pass123", user_db))
print(user_db)
# Attempt to login
print(Login("user1", "pass123", user_db))
print(Login("user1", "wrongpass", user_db))