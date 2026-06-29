#18.reverse keys and values in dictionary.

Player={
    "rohit":45,
    "virat":18,
    "bumrah":93
}

reverse_dictionary={}
for key,value in Player.items():
    reverse_dictionary[value]=key
print("reversed keys and values =",reverse_dictionary)

#19.update value for specific key.

Player.update({"virat":"king"})
print("key value changed =",Player)