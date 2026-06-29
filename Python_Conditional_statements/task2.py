#Grade calculator based on marks:90+ =A,80+B,else C.

Mark=int(input("Enter your marks :"))

if Mark>=90:
    print("Your grade is A")
elif Mark>=80 and Mark<90:
    print("Your grade is B")
else:
    print("Your grade is C")
