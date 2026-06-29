#function to calculate simple interest.   
R=5 
def SI(P,T):
    return ((P*R*T)/100) 
P=int(input("enter a principal Amount : "))
T=int(input("enter a duration Time in year : "))
print("The simple interest is : ",SI(P,T))

