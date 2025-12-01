db = []

def sign_up():
    username = input("Enter your username: ")
    #username validation check
    if not username.islower():
        print("❌ Username must be lowercase!")
        return
    email = input("Enter your email: ")
    #email validation check
    if "@gmail.com" not in email:
        print("❌ Invalid email! Must contain @gmail.com")
        return
    password = input("Enter your password: ")
    #password validation check
    if len(password) < 8:
        print("Must be have 8 charactors!")
        return
    
    db.append({
        "username":username,
        "email":email,
        "password":password
    })
    print("Successfully signup ")
    print(db)


sign_up()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in db:
        if user["username"] == username and user["password"] == password:
            print("Login successfully", username)
            return
    print("Invalid username and password")

print(login())