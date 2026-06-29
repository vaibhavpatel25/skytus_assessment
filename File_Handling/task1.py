# Write program to read a file and display its contents.
 
with open("task1.txt","r") as f:
    text=f.read()
print(text)