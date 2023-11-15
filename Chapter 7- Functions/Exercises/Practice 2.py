#Write a Python function that calculates the factorial of a given positive integer using recursion.

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)
number = 9
outcome = factorial(number)

print(outcome)
