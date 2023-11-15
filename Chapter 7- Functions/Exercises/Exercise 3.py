#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(shirt_size, shirt_message):
    print(f"\nI'm gonna make a {shirt_size} shirt.")
    print(f'It will include, "{shirt_message}"')

make_shirt('medium', 'Python is my favorite language')
make_shirt(shirt_size='Extra Large', shirt_message='Python Tricks.')
