print("Dictionary in Python")

user = {
    "name": "John Doe",
    "age": 25,
    "courses": ["Math", "Science", "Art"]
}
print(user)
print(user["name"])
print(user.get("age"))
print(user.pop("age"))
print(user)
# print(user.keys("age", 25))
user["age"] = 26
print(user)
