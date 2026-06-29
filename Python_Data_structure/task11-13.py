#11.create a dictionary storing student name and marks.

student={
    "Shiv":85,
    "Man":80,
    "Kunjan":70,
    "Shivam":75
    }
print("the dictionary storing student name and marks =",student)

#12.Add new key-value pair to an existing dictionary

student.update({"Vansh":74})
print("the new key-value are added =",student)

#13.delete key-value pair from dictionary.

del student["Vansh"]
print("the one key-value pair were deleted =",student)


