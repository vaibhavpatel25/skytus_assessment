#Atm withdraw system
Atm_number=12345678
Set_Pin=888222
Balance=1000
Card_number=int(input("enter a card number :"))
Pin=int((input("enter your pin :")))
if Pin==Set_Pin and Card_number==Atm_number:
    Amount=int(input("enter a amount :"))
    if Amount==Balance or Amount<Balance:
        print("Transaction Success")
    else:
        print("You have Not enough balance")
else:
    print("Invalid pin")