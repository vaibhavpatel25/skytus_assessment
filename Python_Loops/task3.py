# Find factorial of a number.

N=int(input("Enter a number :"))
fact=1
if N==1 or N==0:
    fact=1
while N>0:
    fact=fact*N
    N-=1
print(fact)
