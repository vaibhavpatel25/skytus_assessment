#17.find the key with the maximum value in dictionary.

Marks={
 "kunjan":70,
 "vansh":74,
 "man":80,
 "shivam":76
}

key=max(Marks,key=Marks.get)
print(f"Key with maximum value :{key}:{Marks[key]}")
