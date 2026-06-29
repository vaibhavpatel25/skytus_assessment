# Check if number is prime or not.

Num=int(input("enter a number :"))

for i in range(2,Num):
    if Num%i==0:
        print(f"The number {Num} is not prime")
        break
else:
   print(f"The number {Num} is prime")
    