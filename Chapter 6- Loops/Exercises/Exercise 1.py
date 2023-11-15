#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.

pizza_prompt = "\nWhat toppings do you want on your pizza? \nType 'quit' when you're done: "

while True:
    topping = input(pizza_prompt)
    if topping != 'quit':
        print(f"\nSure, I'll put {topping} to your pizza.")
    else:
        break