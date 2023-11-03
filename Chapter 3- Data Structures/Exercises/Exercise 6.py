## Exercise 6: Shrinking Guest List :ballot_box_with_check:

invitees = ['Alexis', 'Arnie', 'Arniezza', 'Amara', 'Ali']

message1 = (f"Hello, {invitees[0]}. Would you like to come over for dinner tonight?")
print(message1)

message2 = (f"Hello, {invitees[1]}. Would you like to come over for dinner tonight?")
print(message2)

message3 = (f"Hello, {invitees[2]}. Would you like to come over for dinner tonight?")
print(message3)

message4 = (f"Hello, {invitees[3]}. Would you like to come over for dinner tonight?")
print(message4)

message5 = (f"Hello, {invitees[4]}. Would you like to come over for dinner tonight?")
print(message5)

message4 = f"\nSadly, {invitees[0]} cannot make it tonight."
print(message4)

del(invitees[0])
invitees.insert(0, 'Ariza')

message1 = (f"\nHello, {invitees[0]}. Would you like to come over for dinner tonight?")
print(message1)

message2 = (f"Hello, {invitees[1]}. Would you like to come over for dinner tonight?")
print(message2)

message3 = (f"Hello, {invitees[2]}. Would you like to come over for dinner tonight?")
print(message3)

message4 = (f"Hello, {invitees[3]}. Would you like to come over for dinner tonight?")
print(message4)

message5 = (f"Hello, {invitees[4]}. Would you like to come over for dinner tonight?")
print(message5)

message6 = ("\nMy apologies, I can only invite two people because the dinner table will not be here in time.")
print(message6)

message7 = f"\nI'm sorry, {invitees[0]}. I can only accomodate two people."
invttn =invitees.pop(0)
print(message7)

message8 = f"I'm sorry, {invitees[0]}. I can only accomodate two people."
invttn =invitees.pop(0)
print(message8)

message9 = f"I'm sorry, {invitees[0]}. I can only accomodate two people."
invttn =invitees.pop(0)
print(message9)

invitation1 = f"\nHello, {invitees[0]}. I want to let you know that you're still invited to the dinner tonight."
print(invitation1)   

invitation2 = f"Hello, {invitees[1]}. I want to let you know that you're still invited to the dinner tonight."
print(invitation2)

del(invitees[0])
del(invitees[0])

print(invitees)
