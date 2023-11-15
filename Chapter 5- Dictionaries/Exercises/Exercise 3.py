#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {'Dictionary': 'Unordered key-value data collection.',
            'Tuples': 'Immutable ordered sequence of items.',
            'List': 'Mutable ordered sequence of items',
            'Pseudocode': 'Informal Python Algorithm Planning Language.',
            'Sequences': 'A set of items arranged in a certain order. ',
            'Variables': 'Containers for storing and managing data.',
            'Integer': 'A whole number.',
            'Float': 'A decimal number.',
            'String': 'Text data type.',
            'Turtle': 'Graphics library for drawing shapes.',}
for key, description in glossary.items():
    print("\n"+ key + ": " + description)