# condtional statement practice
"""
card_insert = True
pin = "134"
if card_insert:
    if pin == "1234":
        print("Access Granted")
    else:
        print("Invalid PIN")
else:
    print("Please insert your card")


marks = 70
test_passed_marks = 50
if marks >= 70:
    if test_passed_marks:
        print("Grade A")
    else:
        print("Test not passed")
elif marks >= 50:
    print("Grade B")
else:
    print("Fail")


user_login = False
Item_in_stock = True
if user_login is True:
    if Item_in_stock is True:
        print("Purchase Successful")
    else:
        print("Item Out of Stock")
else:
    print("Please login to continue")


age = 20
has_parental_permission = True
if age >= 18:
    if has_parental_permission:
        print("Access Granted")
    else:
        print("Access Denied: Parental Permission Required")
else:
    print("Access Denied: Underage")


Degree = True
Experience_year = 1
if Degree == True:
    if Experience_year >= 2:
        print("Eligible for Job Interview")
    else:
        print("Not enough experience")
else:
    print("Degree required")

# Task 1: Login System
# username = str(input("Enter username: "))
# password = str(input("Enter password: "))
# is_blocked = True
# if is_blocked == True:
#     if username == "admin" and password == "admin123":
#         print("Login Successful")
#     else:
#         print("Invalid Credentials")
# else:
#     print("Account is blocked")



# Task 2: Scholarship Eligibility
marks = 89.99
sports_certificate = True
family_income= 50000
if marks >= 90:
    if sports_certificate == True and family_income <= 50000:
        print("Eligible for Scholarship")
    else:
        print("Not eligible for Scholarship")
else:
    print("Marks not sufficient for Scholarship")

total_marks = int(input("Enter total marks: "))
sports_certificate = False
family_income= int(input("Enter family income: "))
if total_marks >= 85 or sports_certificate == True:
    if family_income <= 50000:
        print("Eligible for Scholarship")
    else:
        print("Not eligible for Scholarship due to high family income")
else:
   print("Not eligible for Scholarship due to low marks and no sports certificate") 

# Task 3: Online Shopping Checkout
Login_status = True
card_item = 1
payement_successful = True
if Login_status == True:
    if card_item >=1 and payement_successful == True:
        print("Order Placed Successfully")
    else:
        print("Order Failed")
else:
    print("Please login to continue shopping")

# Task 4: Exam Result Evaluation
attendance = 80
persontage = 90
if attendance >= 70:
    print("Eligible for Exam")
    if persontage >= 90:
        print("Grade A")
    elif persontage >= 80:
        print("Grade B")
    elif persontage >= 70:
        print("Grade C")
    else:
        print("Fail, because of low percentage")
else:
    print("Not Eligible for Exam due to low attendance")


# condtional practice end
user_age = int(input("Enter yor age: "))
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

hair = str(input("Enter hair cutting: ").lower())
if hair == "long":
    print("You can get a discount on hair cutting.")
else:
    print("No discount available for short hair.")
"""
password = str(input("Enter your password: "))
if password == "secure123":
    print("Access granted.")
else:
    print("Access denied. Incorrect password.")

