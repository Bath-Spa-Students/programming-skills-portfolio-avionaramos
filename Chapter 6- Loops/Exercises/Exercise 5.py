#Using the list sandwich_orders from Exercise 4, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['chicken sandwich', 'pastrami sandwich','egg sandwich', 'pastrami sandwich',
                   'ham sadnwich', 'pastrami sandwich','nutella sandwich']
finished_sandwiches = []

print("Sadly, deli has run out of pastrami.")
while 'pastrami sandwich' in sandwich_orders: 
    sandwich_orders.remove('pastrami sandwich')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}.")