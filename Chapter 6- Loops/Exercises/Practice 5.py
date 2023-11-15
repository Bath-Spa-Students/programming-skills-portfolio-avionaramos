#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.

largest_number = None

while True:
    user = input("Enter a number (enter '0' to exit): ")
    if user == '0':
        break
    number = float(user)
    if largest_number is None or number > largest_number:
        largest_number = number
if largest_number is not None:
    print(f"Largest Number: {largest_number}")
else:
    print("None.")

