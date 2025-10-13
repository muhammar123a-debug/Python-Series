a = 2
if a % 2 == 0:
    print("even number")
else:
    print("odd number")

b = -1
if b > 0:
    print("positive number")
elif b < 0:
    print("negative number")
else:
    print("zero")

c = 17
if c < 18:
    print("You must be 18+ to drive, you are not eligible")
elif c == 18:
    print("You are eligible to drive")
else:
    print("You can drive")

d = 10
e = 19

if d > e:
    print("d is greater than e")
elif d < e:
    print("d is less than e")
else:
    print("d is equal to e")

f = 96
if f >= 90:
    print("A+")
elif f >= 80:
    print("A")
elif f >= 70:
    print("B")
elif f >= 60:
    print("C")
else:
    print("Fail")
