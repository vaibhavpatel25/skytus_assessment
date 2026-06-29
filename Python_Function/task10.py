#function to check armstrong number.

def armstrong_num(num,digits):
    sum=0
    if num==0:
        return 0
    digit=num%10
    sum=sum+digit**digits
    return sum + armstrong_num(num//10,digits)
    
num=int(input("enter the number : "))
digits=len(str(num))
if armstrong_num(num,digits)==num:
    print(f"the number {num} is armstrong")
else:
    print(f"the number {num} is not armstrong")