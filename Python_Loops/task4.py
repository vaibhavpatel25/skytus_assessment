# Generate First fibonacci numbers.

N=int(input("enter a number :"))
a=0
b=1

for i in range(N):
    print(a, end=" ")
    c=a+b
    a=b
    b=c