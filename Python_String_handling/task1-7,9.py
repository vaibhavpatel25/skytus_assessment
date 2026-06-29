#1.Take a string input and print it's length.

String=input("Enter a string :")
print("the length of string :",len(String))

#2.Convert a sentence to lowercase.
 
print("String in lowercase =",String.lower())

#3.Replace spaces with underscores in a string.

print("Replaced command =",String.replace(" ","_"))
 
#4.Extract the first and last character of a string.
 
print("First : ",String[0])
print("Last : ",String[-1])

#5.Reverse a string using slicing .

print("reversed string =",String[ : :-1])

#6.count how many time a letter appears in a string.

print("Count letters :",String.count("a"))

#7.Check if a word is present in a sentence.

print("Is present :","ai" in String)

#9.Remove extra spaces from the start and end of string.
 
print("remove space =",String.strip())





