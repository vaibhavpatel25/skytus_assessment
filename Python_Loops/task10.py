#Find all divisors of number.

N=int(input("Enter a number :"))

Divisors=[]
for i in range(1,N+1):
    if N%i==0:
        Divisors.append(i)
print("The divisors of number =",Divisors)
    