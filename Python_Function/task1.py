#function to check the number is prime or not.

def prime(n):
    if n<=1:
            print(f"The number {n} is not prime")
    else:
        for i in range(2,n):
        
            if n%i==0:
               print(f"The number {n} is not prime")
               break
        else:
            print(f" the number {n} is prime")

n=int(input("enter a number :"))
prime(n)
