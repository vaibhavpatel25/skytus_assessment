# find sum of even numbers between(1-100)
sum=0
for num in range(1,101):
    if num%2==0:
        sum+=1
print("The sum of even numbers :",sum)