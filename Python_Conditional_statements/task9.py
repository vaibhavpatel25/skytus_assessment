#simple calculator (add,substract,multiply,divide)

Num1=float(input("Enter a number :"))
Num2=float(input("Enter a number :"))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=input("Enter your choice =")

if choice=="1":
    print("Addition :",Num1+Num2)
elif choice=="2":
    print("Substraction :",Num1-Num2)
elif choice=="3":
    print("Multiplication :",Num1*Num2)
elif choice=="4":
    if Num2!=0:
        print("Division :",Num1/Num2)
    else:
        print("Cannot divide by 0")
else:
    print("invalid choice")