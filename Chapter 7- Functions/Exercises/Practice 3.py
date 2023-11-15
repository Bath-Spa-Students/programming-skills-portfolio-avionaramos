#Write a Python program that uses a function to check if a given number is prime or not.

def is_prime(number):
    if number < 4:
        return False
    for i in range(4, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
given_number = 20
if is_prime(given_number):
    print(f"{given_number} is a prime number.")
else:
    print(f"{given_number} isn't a prime number.")
