#Write a Python program to iterate through both the keys and values of a dictionary and print them 

information = {'name' : 'Aviona',
               'Surname' : 'Ramos',
               'Age' : '18',
               'Nationality' : 'Philippines',
               'Hobbies' : 'sleeping'}
for key, value in information.items():
    print(f"{key}: {value}")