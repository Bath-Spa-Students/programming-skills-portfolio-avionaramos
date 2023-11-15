#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet

pet1 = {'animal' : 'Dog', 'animal type': 'Doberman','owner': 'Tom'}
pet2 = {'animal': 'Bird','animal type': 'Parrot','owner': 'Amara'}
pet3 = {'animal': 'Cat','animal type': 'Persian','owner': 'Alexis'}

pets = [pet1, pet2, pet3]

# loop through the list and print information about each pet
for pet in pets:
    print(f'This {pet["animal"]} is a {pet["animal type"]} owned by {pet["owner"]}.')
   
