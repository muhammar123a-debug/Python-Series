# # Problem: Conditional Check (Weird or Not Weird)
# n = int(input("Enter a number:"))
# if n % 2 != 0:
#     print("Weird")
# else:
#     if n >= 2 and n <= 5:
#         print("Not Weird")
#     elif n >= 6 and n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")
    
x = str(input("Enter your id: "))
if x == "BSE206":
    print("Welcome Shayan")
else:
    print("You are not Enrol")


# BASIC PRACTICE 
import pandas as pd 
df = pd.read_excel("students.xlsx")

def get_grades(avg):
  if avg >= 80:
    return "A"
  elif avg >= 70:
    return "B"
  elif avg >= 60:
    return "C"
  elif avg >= 50:
    return "D"
  else:
    return "F"

def student_analyzer():
  while True:
    print("\n ===== Student Analyzer Menu =====")
    print("1. Total Students")
    print("2. pass/fail (all student)")
    print("3. count pass & fail")
    print("4. subject-wise average")
    print("5. topper")
    
    choice = int(input("\nEnter Choice: "))

    if choice == 1:
      print("Total student", len(df))
    elif choice == 2:
      for i, row in df.iterrows():
        if row["Math"] >= 50 and row["Physics"]>= 50 and row["English"] >= 50 and row["CS"]>= 50:
          print(row["Name"] + "=> Pass")
        else:
          print(row["Name"] + "=> Fail")
    elif choice == 3:
      passed = 0
      failed = 0
      for i, row in df.iterrows():
        if row["Math"] >= 50 and row["Physics"]>= 50 and row["English"] >= 50 and row["CS"]>= 50:
          passed += 1
        else:
          failed += 1
      print("Total Passed:",passed)
      print("Total Failed:", failed)

    elif choice == 4:
      print("Math Avg", df["Math"].mean())
      print("Physics Avg", df["Physics"].mean())
      print("English Avg", df["English"].mean())
      print("CS Avg", df["CS"].mean())

    elif choice == 5:
      df["Total"] = df[["Math","Physics","English","CS"]].sum(axis=1)
      topper = df.loc[df["Total"].idxmax()]
      print("Topper:", topper["Name"], "| Total Marks:", topper["Total"])

