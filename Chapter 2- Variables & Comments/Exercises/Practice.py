# Homogeneous List / Python Supports Heterogenous List other than C , Java
hotdog =["Amara", "Tomato", "Ali", "Alexis"]
print(hotdog)

#Heterogenous 
cheesedog = ["Noodles", "10", "Egg", "2.5"]
print(cheesedog)

# Repetition operators
egg = [9] * 7
print(egg)

# Indexing
numbers =[2,1,9,5,4]
print(numbers[2])

# Negative Indexing
numbers =[2,1,9,5,4]
print(numbers[-2])

# lens function
numbers =[2,4,7,5,9,1,3,6]
print("number of elements in a list:", len(numbers))

# Mutability (Changeable)
numbers = [10,27,20,24,21,26,12,29,2,8,9]
numbers[2]= 3
numbers[5]= 11
print(numbers)

# Concatentation
sushi = [2,4,6,7,8]
ramen = [9,7,5,3,1]
mango= sushi + ramen
print(mango)

# Slice
pizza = [4,5,1,3,7,8,2,9]
result = pizza [4:7]
print(result)

# 
burger = [4,5,1,3,7,8,2,9]
if 11 in burger:
    print("lesgaur")
else:
    print("naur")



