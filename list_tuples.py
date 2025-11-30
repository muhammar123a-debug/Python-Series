print("List and Tuples")

numbers = [12, 75, 150, 180, 45, 22, 90, 101]
count = 0
for num in numbers:
    if num > 50:
        count += 1
print(f"Count of numbers greater than 50: {count}")

nums = [2, 7, 12, 19, 24, 28, 31, 40]
even_num = [nums for nums in nums if nums % 2 == 0]
print(f"Even numbers from the list: {even_num}")

marks = [78, 45, 98, 60, 89, 99, 58]
max_marks = marks[0]
for mark in marks:
    if mark > max_marks:
        max_marks = mark
print(f"Maximum marks obtained: {max_marks}")

items = [1,2,3,2,4,5,3,6,4,7]
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print(f"List after removing duplicates: {unique_items}")


names = ["Ali", "Bilal", "ammar", "Sara", "Arslan", "zain"]
for i in names:
    if i.startswith("A") or i.startswith("a"):
        print(i)

words = ["apple", "banana", "grapes", "orange"]
count = 0
vowels = "aeiou"
for word in words:
    for char in word:
        if char in vowels:
            count += 1
print(f"Number of words that are vowels: {count}")

shopping = ["Bread", "Milk", "Eggs"]
update = shopping.append("Butter")
print(f"Updated shopping list: {shopping}")


    