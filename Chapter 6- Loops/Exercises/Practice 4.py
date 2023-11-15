#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

for numbers in range(1, 50):
    if numbers > 5 and numbers % 2 == 0:
        print(f"First even number greater than 5 is: {numbers}")
        break