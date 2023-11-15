#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

rivers = {'Murray': 'Australia',
          'Volga': 'Russia',
          'Yangtze': 'China'}
for key, country in rivers.items():
    print("The " + key + " passes through " + country)
print("\n")
for key, country in rivers.items(): 
    print("Rivers: " + key)
print("\n")
for key, country in rivers.items():
    print("Countries: " + key)

