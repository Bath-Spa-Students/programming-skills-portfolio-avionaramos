#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(shirt_size = 'Small', shirt_message = 'I love Python'): 
    print(f"\nI'm gonna make a {shirt_size} shirt.")
    print(f'It will include, "{shirt_message}"')

make_shirt()
make_shirt(shirt_size='Medium')
make_shirt('Large', 'Lets go!!')
