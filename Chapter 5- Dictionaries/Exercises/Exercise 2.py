#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {'Dictionary': 'Unordered key-value data collection.',
            'Tuples': 'Immutable ordered sequence of items.',
            'List': 'Mutable ordered sequence of items.',
            'Pseudocode': 'Informal Python Algorithm Planning Language.',
            'Sequences': 'A set of items arranged in a certain order. ',}

print("\n"+ "Dictionary: " + glossary["Dictionary"])
print("\n"+ "Tuples: " + glossary["Tuples"])
print("\n"+ "List: " + glossary["List"])
print("\n"+ "Pseudocode: " + glossary["Pseudocode"])
print("\n"+ "Sequences: " + glossary["Sequences"])