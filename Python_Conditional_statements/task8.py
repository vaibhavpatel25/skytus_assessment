#electricity bill calculator based on units consumed.

Units=int(input("Enter consumed units :"))
'''
first 100 units :rate 5 rupees per unit
after 100 units :rate 7 rupees per unit
after 200 units :rate 10 rupees per unit
'''

if Units<=100:
    Bill=Units*5
elif Units<=200:
    Bill=(100*5)+((Units-100)*7)
else:
    Bill=(100*5)+(100*7)+((Units-200)*10)
 
print(f"Electricity Bill = {Bill} rupees")
    