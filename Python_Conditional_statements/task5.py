#Check if a number is positive ,negative or zero.

Number=int(input("Enter a number :"))

if Number>0:
    print(f"The Number {Number} is Positive ")
elif Number<0:
    print(f"The Number {Number} is Negative")
else:
    print("The Number is zero")