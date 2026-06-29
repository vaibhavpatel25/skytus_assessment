#function to find gcd of two numbers.
def gcd(num1,num2):
    GCD=1
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            GCD=i  
    return GCD
num1=int(input("enter a first number :"))
num2=int(input("enter a second number :"))
print(f"the GCD of {num1} & {num2} is {gcd(num1,num2)}")