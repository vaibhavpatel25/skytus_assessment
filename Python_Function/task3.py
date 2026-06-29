#function to find factorial.
fact=1
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n*factorial(n-1)

n=int(input("enter a number :"))
print(f"the factorial of {n} is :{factorial(n)}")