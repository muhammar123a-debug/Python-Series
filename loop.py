for i in range(5):
    print("Iteration:", i)

for j in range(1, 6):
    print("Count:", j)

for k in range(0, 10, 2):
    print("Even number:", k)

for m in range(10, 0, -1):
    print("Countdown:", m)

for t in range(1, 11):
    print(f"7 x {t} = {t * 7}")

# Sum of numbers 1 to 50
sum = 0
for n in range(1, 51):
    sum += n
print("Total Sum from 1 to 50:", sum)

# looping in list
fruits = ["apple","banana","cherry"]
for im in fruits:
    print("Fruit:", im)

numbers = [12, 5, 7, 20, 33, 42, 9, 10]
for i in numbers:
    if i % 2 == 0:
        print("Even number in list:", i)

items = ["apple", "banana", "mango", "grapes", "orange", "kiwi"]
count = 0
for i in items:
    count += 1
print("Total items in the list:", count)

nums = [45, 12, 99, 23, 77, 150, 3, 88]
max = 0
for n in nums:
    if n > max:
        max = n
print("Maximum number in the list:", max)

names = ["Ali", "Ammar", "Bilal", "Anas", "Sara", "Ayesha", "Zain"]
count_a = 0
for name in names:
    if "a" in  name.lower():
        count_a += 1
print("Names containing 'a':", count_a)


prices = [50, 120, 300, 90, 45, 150, 220, 80]
total_price = 0
for price in prices:
    if price < 100:
        total_price += price
print("Total price of items less than 100:", total_price)

texts = "The quick brown fox jumps over the lazy dog"
vowel_count = 0
for char in texts.lower():
    if char in "aeiou":
        vowel_count += 1
print("Total number of vowels in the string:", vowel_count)


text = "Ammar123Hello9"
digit_count = 0
for ch in text:
    if ch.isdigit():
        digit_count += 1
print("Total number of digits in the string:", digit_count)

name = "Ammar"
reverse = ""
for char in name:
    reverse = char + reverse
    print("Intermediate reverse:", reverse)
print("Reversed string:", reverse)

text = "Hello World"
search_char = str(input("Enter a character to search: "))
found = False
for ch in text:
    if ch == search_char:
        found = True
        break
if found:
    print(f"The character '{search_char}' is found in the string.")
else:
    print(f"The character '{search_char}' is not found in the string.")


for u in range(1, 6):
    print("*"*u)

for v in range(5,0,-1):
    print("*"*v)

for i in range(1, 50):
    print(f"7 x {i} = {1 * 7}")

for p in range(1, 31):
    if p % 3 == 0 and p % 5 == 0:
        print("FizzBuzz")
    elif p % 3 == 0:
        print("fizz")
    elif p % 5 == 0:
        print("Buzz")
    else:
        print(p)
count_division_by_3 = 0
for q in range(1, 51):
    if q % 3 == 0:
        count_division_by_3 += 1
        
print("Total numbers divisible by 3 from 1 to 50:", count_division_by_3)

list = [12, 45, 67, 22, 90, 33, 50, 97]
larg_even = 0
for num in list:
    if num % 2 == 0 and num > larg_even:
        larg_even = num
print("Largest even number in the list:", larg_even)

list_name = ["Ali", "Ammar", "Bilal", "Anas", "Sara"]
count_i = 0
for n in list_name:
    if "i" in n.lower():
        count_i += 1
        print(n)
print("Names containing 'i':", count_i)

list = [15, 22, 33, 40, 7, 55, 60]
for item in list:
    if item > 50:
        break
    print("Item:", item)

# Print numbers “Even Large” or “Odd Small”
for i in range(1, 21):
    if i % 2 == 0  and i > 10:
        print(i, "Even Large")
    elif i % 2 != 0 and i < 10:
        print(i, "Odd Small")
    else:
        print(i)

# Software-Oriented Logical Loop Questions
# Question 1 — Bank ATM Simulation
attempts = 3
while attempts > 0:
    pin = int(input("Enter your 4-digit PIN: "))
    if pin == 4321:
        print("Access Granted. Welcome to your account!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN. Try again.")
if attempts == 0:
    print("Account locked due to too many incorrect attempts.")

