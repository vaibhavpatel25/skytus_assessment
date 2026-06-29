# Count digits in number.

Num=int(input("enter a number :"))
count=0

while Num>0:
    Num=Num//10
    count+=1
print("Total digits :",count)
