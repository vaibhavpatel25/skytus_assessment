# reverse numbers (eg.123 -> 321)
Num=int(input("enter a number :"))
reverse=0
while Num>0:
  digit=Num%10
  reverse=reverse*10+digit
  Num=Num// 10
print("Reversed number :",reverse)