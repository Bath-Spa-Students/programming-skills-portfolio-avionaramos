# Write a Python program to merge two dictionaries into one.

information1 = {'name' : 'Aviona', 'Surname' : 'Ramos', 'Age' : '18',}
information2 = {'Nationality' : 'Philippines', 'Hobbies' : 'sleeping'}

merged_dict = information1.copy()  
merged_dict.update(information2)

print(merged_dict)
