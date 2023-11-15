#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket

age_prompt = ("Good day! May I know you age? \nType 'quit'when you're done: ")

while True:
    age = input(age_prompt)
    if age =='quit':
        break
    age = int(age)
    if age < 3:
        print("Hello, good day! Your ticket is free!")
    elif age < 13:
        print("Hello, good day! Your ticket cost 10$.")
    else:
        print("Hello, good day! Your ticket cost 15$.")
   