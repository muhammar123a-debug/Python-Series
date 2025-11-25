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

