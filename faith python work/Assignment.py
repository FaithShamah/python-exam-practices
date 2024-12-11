student_names = ["Sandra", "Patricia", "Phionah", "Anitah"]
student_mark = [80,56,78,90]
# Print from Patricia, Faith, Phionah, Anitah.
student_names.insert(2,"Faith")
student_names.remove("Sandra")
print(student_names)

# Add marsha at the 4th position
student_names.insert(3,'Masha')
print(student_names)

# Update the name Phionah to Aladina
student_names[student_names.index("Phionah")] = "Aladina"
print(student_names)

# Display the length of the students list
print("Length of the student names list:", len(student_names))

# Print all the students names using a four loop
for name in student_names:
    print(name)

# Calculate the total marks for the student mark variable(Ans.304)
total_marks = sum(student_mark)
print("Total marks:", total_marks)  
