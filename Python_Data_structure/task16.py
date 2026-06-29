#16.count word frequency in a given string using dictionary,

string="apple banana mango banana apple banana"

words=string.split()
frequency={}
for word in words:
    if word in  frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)
    