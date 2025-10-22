
user_db = {}
def register_user(username, password, user_id):
    if username in user_db:
        return "Username already exists."
    user_db[username] = {'password': password, 'user_id': user_id}
    return "Registration successful."

def login_user(username, password, user_db):
    if username not in user_db:
        return "Username does not exist."
    if user_db[username]["password"] != password:
        return "Incorrect password."
    return "Login successful."

register_user("john_doe", "securepassword", "JD123")
register_user("Ammar", "securep", "JD125")
register_user("anas", "secu", "JD4")
print(user_db)  # Should show the registered user details
print(login_user("john_doe", "securepassd", user_db))  # Should print "Login successful."