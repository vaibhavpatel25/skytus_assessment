#Print a pyramid pattern.
N=int(input("enter a number :"))

for i in range(1,N+1):
    print(f" "*(N-i),end="")
    print(f"*"*((2*i)-1))