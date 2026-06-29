#function to count vowels in string.

def vowels(string):
    count=0
    for i in string:
        if i in "aeiouAEIOU":
             count+=1
    return count
string=input("enter a string :")
print("the count of vowels :",vowels(string))