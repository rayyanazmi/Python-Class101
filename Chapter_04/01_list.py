# Python lists are containers to store a set of values of any data type.

friends = ["Apple","Orange", 5, 32.07, False, "Rayyan", "Azmi"]

print(friends)
friends[0] = "Grapes" # Unlike string list is mutable
print(friends[0])
print(friends[1:5])

friends.append("Human") # Append will combine the given input at the last of list
print(friends)
