#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.

month = (input("Enter the month: "))

if month in ["December", "January", "February"]:
    print(f"The season for {month} is winter")
elif month in ["March", "April", "May"]:
    print(f"The season for {month} is spring")
elif month in ["June", "July", "August"]:
    print(f"The season for {month} is summer")
elif month in ["September", "October", "November"]:
    print(f"The season for {month} is fall")
else:
    print("Invalid Month")






