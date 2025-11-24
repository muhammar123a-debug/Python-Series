# condtional statement practice

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
