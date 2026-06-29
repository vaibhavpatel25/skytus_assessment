#ATM withdrawal ckeck: sufficient balance or not.

balance=10000
Amount=int(input("Enter amount to withdraw :"))

if Amount<=balance:
    print("Withdrawal successful")
else:
    print("You have Insufficient balance")