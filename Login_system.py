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
    if username not in db:
        print("Your username is not exists")
        return
    email = input("Enter your email: ")
    if email not in db:
        print("Your email is not exist")
        return
    password = input("Enter your password: ")
    if password not in db:
        print("Your password is wrong")
        return
    
    print("Login successfully")

print(login())