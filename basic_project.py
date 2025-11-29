# ATM system 
"""
balance = 25000
pin = 1234

def atm():
    global balance
    user_pin = int(input("Enter your Pin: "))

    if user_pin != pin:
        print("Incorrect Pin")
        return
    
    while True:
        print("\n 1. Check Balance \n 2. Withdraw Money \n 3. Deposit Money \n 4. Exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            print(f"your balance is: {balance}")
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print(f"Please collect your cash. New balance is: {balance}")
        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"Amount deposited successfully. New balance is: {balance}")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
print(atm())



# Student Result Management

student = []
def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(3):
        mark = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    persontage = sum(marks)/3
    student.append({"name":name, "marks":marks, "persontage":persontage})

def display_students():
    for stud in student:
        print(stud)

while True:
    print("\n 1. Add Student \n 2. Display Students \n 2. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

"""
# Shopping Cart Billing System
cart = []

def add_item():
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    cart.append({"name": item_name,"price": item_price})

def display_cart():
    total = 0
    print("\nItems in your cart:")
    for item in cart:
        if item["price"] > 2000:
            discount = item["price"] *0.10
            final_price = item["price"] - discount
            print(f"{item['name']}: Original Price: {item['price']}, Discounted Price: {final_price}")
            total += final_price
        else:
            print(f"{item['name']}: Price: {item['price']}")
            total += item["price"]
    print(f"Total amount to be paid: {total}")
while True:
    print("\n 1. Add Item \n 2. Display Cart \n 3. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        display_cart()
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    