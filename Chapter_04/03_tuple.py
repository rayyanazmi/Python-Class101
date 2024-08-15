# A tuple is an immutable data type in python.

a = (1, 45, 365, 45, 24, 9, False, "Rayyan")
print(a)

no = a.count(45)
print(no)

no = a.index(24) # tuple.index will locate the item index from the tuple
print(no)

repeated = a * 3
print(repeated)

print(len(a))
