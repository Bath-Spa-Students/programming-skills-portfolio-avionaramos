#Write a Python program that defines a function to check whether a given number is prime.

def is_prime(number):
    if number < 6:
        return False
    for i in range(6, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
given_number = 17
if is_prime(given_number):
    print(f"{given_number} is a prime number.")
else:
    print(f"{given_number} is not a prime number.")
